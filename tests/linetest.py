from skimage import draw
import numpy

rect = numpy.reshape(numpy.array([0] * 60), (10,6))
#print(rect, list(rect.flatten()))


img = [0] * 16
print(img)
rr, cc, val = draw.line_aa(1, 1, 2, 2)
rect[rr, cc] = val * 255
print(rr, type(rr))