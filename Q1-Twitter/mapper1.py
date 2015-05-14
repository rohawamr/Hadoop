#!/usr/bin/env python

import sys
import string
import json
from pprint import pprint

dates = 4000*[0]
hours = 24*[0]
date_count = 0

for line in sys.stdin:
  try:
    tweet = json.loads(line)
    timeStamp = tweet['created_at'].split();
    date = timeStamp[1]+" "+timeStamp[2]+" "+timeStamp[5]
    time = timeStamp[3]
    hour = int(time.split(':')[0])
    if date not in dates:
      dates.append(date)
    hours[hour] += 1
  except:
    continue


for pr in range(len(hours)):
  print '%s\t%s' % (pr,hours[pr])

for d in range(len(dates)):
  if dates[d] != 0:
    print 'date\t%s' % (dates[d])
