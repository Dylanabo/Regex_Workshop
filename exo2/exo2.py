#!/usr/bin/python
import re

pattern = '([main :])+\{.*?[\n]\}'
patternToIgnore = '^#'
file = open('exo2.txt',mode='r')
all_of_it = file.read()
tab = all_of_it.split('\n')
file.close()
for i in tab:
    result1 = re.findall(pattern, all_of_it)
    result2 = re.findall(patternToIgnore, all_of_it)

if result1:
  print("Search successful. Good format => ")
else:
  print("Search unsuccessful. Invalid Format")