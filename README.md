# DominantColor
Finds the dominant color in a picture, taking into account the dark/white/transparent background.


#Dependencies
Requirements include: scipy, numpy, image

For quick installation use pip

<code>pip install -r requirements.txt</code>

#Initializing
<code>from DominantColor import DominantColor</code>

<code>dc = DominantColor(filename)</code>


#Attributes
hex: returns a string hex color value

rgb: returns a numpy.ndarray sequence
