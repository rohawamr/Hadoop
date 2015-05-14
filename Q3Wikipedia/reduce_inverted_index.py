#!/usr/bin/env python
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    for current_word, group in groupby(data, itemgetter(0)):
        fileList = ''
        first = True
        for current_word, fileName in group:
            if (not first):
                fileList = fileList + ', '
            first = False
            fileList = fileList + fileName
        print "%s%s%s" % (current_word, separator, fileList)

if __name__ == "__main__":
    main()
