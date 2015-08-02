from PIL.Image import open
from scipy import product, cluster, histogram, argmax
from scipy.misc import fromimage
from scipy.cluster.vq import vq, kmeans
from numpy import delete as np_delete

class DominantColor():
    """
    Instantiate with a filename (For a picture)
    So far png and jpg have been tested, png takes out the alpha element
    Although png is less accurate and slightly changes.
    Returns the dominate color, as long as it is not too dark, or too light
    """

    def __init__(self, file):
        self.NUM_CLUSTERS = 3
        orig_im = open(file)
        self.im = orig_im.resize((150, 150))# reduce time
        self.ar, self.codes = self.generate_scalar()
        self.hex, self.rgb = self.get_dominant()


    def get_luminosity(self, row):
        """
        Determine the luminosity of the image's color clusters
        """
        lum_checker = [.213, .715, .072, .255]
        checker = 0.0
        for index, rgba in enumerate(row):
            checker += lum_checker[index] * rgba
        return checker


    def generate_scalar(self):
        """
        breaks the image into a multi-dimensional array -> (ar)
        then breaks the rows up by NUM_CLUSTERS & color -> (codes)
        """
        ar = fromimage(self.im)
        shape = ar.shape
        ar = ar.reshape(product(shape[:2]), shape[2])
        float_ar = ar+0.0
        codes, dist = kmeans(float_ar, self.NUM_CLUSTERS)
        return ar, codes


    def get_dominant(self):
        """
        ensures that we don't throw out too dark, or light of images
        which are usually in the background of photos. This comes in
        handy when images are transparent or are a logo
        """
        stop = False
        while stop == False:
            vecs, dist = vq(self.ar, self.codes) # assign codes
            counts, bins = histogram(vecs, len(self.codes))  # count occurrences
            index_max = argmax(counts)
            peak = self.codes[index_max]
            lumin = self.get_luminosity(peak)
            if lumin > 200.0 or lumin < 35.0: # too light, too dark
                self.codes = np_delete(self.codes,(index_max), axis=0)  #retry without that instance
            else:
                stop = True
                rgb = ''.join(chr(int(c)) for index, c in enumerate(peak) if not index == 3)
                dom_hex = "#%s" % rgb.encode('hex')
                rgb = peak[:3]
        return dom_hex, rgb
