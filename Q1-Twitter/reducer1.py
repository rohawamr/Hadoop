import sys
import string
import json
from pprint import pprint

dates = 4000*[0]
date_count = 0
hours = 24*[0]

for line in sys.stdin:
  try:
    (key,val) = line.strip().split('\t',1)
    if key == 'date':
      if str(val) not in dates:
        dates.append(str(val))
        date_count += 1
    else:
      hours[int(key)] += int(val)
  except:
    continue


maxx = max(hours);

for pr in range(len(hours)): 
  if hours[pr] == maxx:
    req = pr+1
  hours[pr] = hours[pr]/date_count
  print '%s\t%s' % (pr,hours[pr])

       
print 'President Ono Tweets most at %s' % (req)
