#!/usr/bin/python
import re

pattern = '[A-Z]+'
file = open('exo1.txt',mode='r')
all_of_it = file.read()
file.close()
result = re.findall(pattern, all_of_it)

if result:
  print("Search successful. All Upper Character => ", *result, sep='')
else:
  print("Search unsuccessful. No Upper Characte")