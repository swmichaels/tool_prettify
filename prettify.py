#!/usr/bin/env python
import sys

try:
    from BeautifulSoup import BeautifulSoup
except:
    sys.exit('Error: could not find BeautifulSoup module. Please type the following: pip install beautifulsoup')    

import fileinput

s = ''
for line in fileinput.input():
    s += line

hi = BeautifulSoup(s)

print hi.prettify()
