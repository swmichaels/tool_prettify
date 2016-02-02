#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup

import fileinput

s = ''
for line in fileinput.input():
    s += line

hi = BeautifulSoup(s)

print hi.prettify()
