from DominantColor import DominantColor

dc = DominantColor("test_image.jpg")
print "R: %s, G: %s, B: %s" % tuple(dc.rgb)
print dc.hex
