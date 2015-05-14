#!/usr/bin/env python

import sys
import string
import json
from pprint import pprint

days = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}

for line in sys.stdin:
  try:
    tweet = json.loads(line)
    timeStamp = tweet['created_at'].split();
    day = str(timeStamp[0])
    days[day] += 1
  except:
    continue

for key, value in days.iteritems():
  print '%s\t%s' % (key,value)
