#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.etree.ElementTree as ET
import chardet


dict = {}
for event, elem in ET.iterparse("txt"):
  s = elem.text
  s = s.split()
  for i in s:
    dict[i] = dict.get(i, 0) + 1


lst = []
for k,v in dict.items():
  if len(k) > 6:
    lst.append([v, k])
  
lst.sort(reverse=True)
lst = lst[:10]
for i in lst:
  print(str(i[0])+":",i[1])

