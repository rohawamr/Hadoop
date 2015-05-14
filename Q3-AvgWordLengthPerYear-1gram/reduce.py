#!/usr/bin/env python

import sys
import string

sum_val = 0
old_word = None
dict1={}

#seperate the key value pairs for both numerator and denominator for each year,and store it in dictionary
# below code aggregates to calculate the sum of input stream Ex. n_1947=sum(values) and d_1947=sum(values)

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	if old_word != key:
		if old_word:
			dict1[old_word]=sum_val         
		sum_val = 0
	old_word = key
	try:
		sum_val = sum_val + int(val)
	except:
		continue

#for each year you will have two values:
	#Ex for 1947: n_1947 and d_1947 keys in dictionary
	#So we need to divide: n_1947/d_1947

dict1[old_word]=sum_val

for k in dict1:
	x=k[2:]                 #to remove "n_" from say "n_1947"
	n=dict1[k]              #then find denominator for a year, ex. "d_1947"
	y=[value for key, value in dict1.items() if x in key.lower()][0]
	if n==y:
		y=[value for key, value in dict1.items() if x in key.lower()][1]
	if n>y:
		d=n/y
	else:                   #divide: n_1947/d_1947
		d=y/n
	print x,d
