#!/usr/bin/env python

import sys
import string
import json
from pprint import pprint

days = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}

for line in sys.stdin:
  try:
    (key,val) = line.strip().split('\t',1)
    days[str(key)] += int(val)
  except:
    continue

maxx = "Sun"

for key,value in days.iteritems():
  if value>days[maxx]:
    maxx = key

       
print 'President Ono Tweets most on %s on an Average' % (maxx)
