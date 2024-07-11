#!/usr/bin/python

# Designed by: Amir Yazdanbakhsh
# Date: March 26th - 2015
# Alternative Computing Technologies Lab.
# Georgia Institute of Technology

import sys
#import random
import math

def Usage():
	print "Usage: python data_generator.py <size>"
	exit(1)

if(len(sys.argv) != 2):
	Usage()

data_size 	= sys.argv[1] 
loc_out 	= open("locations_" + str(data_size) + ".data", 'w')

loc_out.write(str(data_size) + "\n")



for i in range(int(data_size)):
	for j in range(6):
		for k in range(3):
			loc_out.write(str((i+j)%40 + 30 - 50) + " ")
		pass
	pass
	loc_out.write("\n")
pass

print "Thank you..."
