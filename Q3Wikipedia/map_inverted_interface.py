#!/usr/bin/env python
import sys
import string
import re

dic={}

def find(search):
	flag=0
	f=open('part-00000','r')
	for line in f:
		(key,val) = line.strip().split('\t',1)
		if key == search:
			dic[key]=[x.strip() for x in val.split(',')]
			#print val
			flag=1
	if flag==0:
		print 'Not found'



search=raw_input('Enter search string: ')
li=re.split(' and | or ',search)
print li


for l in li:
	find(l)	


for k,v in dic.items():
	print k,v

if 'and' in search:
	inter=set(dic.values()[0]) & set(dic.values()[1])
elif 'or' in search:
	inter=set(dic.values()[0]) | set(dic.values()[1])
print inter
