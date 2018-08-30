#!/usr/bin/python
#version 0.6
import numpy, os, array, PIL
from PIL import Image

filename = raw_input('Enter file here: ')
#filename = 'putty.exe'
f = open(filename,'rb')
ln = os.path.getsize(filename) # length of file in bytes
width = 256
rem = ln%width

a = array.array("B") # uint8 array
a.fromfile(f,ln-rem)
f.close()
g = numpy.reshape(a,(len(a)/width,width))
g = numpy.uint8(g)

im = PIL.Image.fromarray(g)
im.save(filename + ".jpeg")
print "Visualisation completed:" + filename + ".jpeg created"
