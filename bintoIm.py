#!/usr/bin/python
#version 0.6
#Basic Functionality: Input a binary file, create a array of values, convert array to unit8, upload MD5 to virustotal, get Kaspersky malware identifier, save file as jpeg
#
import numpy, os, array, PIL, subprocess, re
from PIL import Image

filename = raw_input('Enter file here: ')
f = open(filename,'rb')                         #opens file as readonly binary
ln = os.path.getsize(filename)                  #Get length of file in bytes
width = 256                                     #Give width as 256 bytes
rem = ln%width                                  #Used for cleanup: variable remainder of length divided by width of image

a = array.array("B") 				#Creates array
a.fromfile(f,ln-rem)				#Read binary file and (length - remainder) as machine values from file into array
f.close()
g = numpy.reshape(a,(len(a)/width,width))	#reshapes the array
g = numpy.uint8(g)				#changes array from int64 to unit8 to allow PIL to process array to image

var = os.popen('/usr/local/sbin/vtlite.py -s ../binary').read()  #Runs VirusTotal API scan on binary
regex = re.compile('Kaspersky Detection: (.*?)\n')		#Create Regular Expression
m = regex.search(var)						#Searchs for reg expression in var output
b = m.group(1)							#Sets var as first subgroup output, i.e. the name of the malware
c = b.strip()   						#strip whitespace

im = PIL.Image.fromarray(g)					#Render the numpy array for visualisation
im.save( c + ".jpeg")						##Save file as JPEG

#print("Visualisation completed:" + m.group(1) +".jpeg created", sep='')
print "Visualisation completed:" + c + ".jpeg created"
