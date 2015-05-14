#!/usr/bin/env python

import sys
import string
import json
from pprint import pprint

for line in sys.stdin:
  try:
		data = json.loads(line)
		uid = data['id_str']
  except:
		continue
  if uid == "211178363":
    print '%s' % (count) 
