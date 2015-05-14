#!/usr/bin/env python

import sys
import string

def mapper():
  for line in sys.stdin:
	num = line.split()
	#print num[1]	    
	print 'n_%s\t%s' % (num[1],(len(num[0])*int(num[3])))    #Numerator- product of (length of word) and (the count)
  	print 'd_%s\t%s' % (num[1],num[3])                       #Denominator- Count of word 



mapper()
