from DominantColor import DominantColor

cg = DominantColor("test_image.jpg")
print "R: %s, G: %s, B: %s" % tuple(cg.rgb)
print cg.hex

