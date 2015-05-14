#!/usr/bin/env python
import sys, os

def read_input(file):
    for line in file:
        yield line.split()

def getFileName():
	if 'map_input_file' in os.environ:
		return os.environ['map_input_file']
	else:
		return 'none'


def main(separator='\t'):
    
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print '%s%s%s' % (word, separator, getFileName())

if __name__ == "__main__":
    main()
