#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_files(fileName):
  import xml.etree.ElementTree as ET
  dict = {}
  for event, elem in ET.iterparse(fileName):
    s = elem.text
    s = s.split()
    for i in s:
      dict[i] = dict.get(i, 0) + 1
  
  return dict
  
def count_word(dict, wordLength):
  lst = []
  for k,v in dict.items():
    if len(k) > wordLength:
      lst.append([v, k])
  return lst



def main():
  dict = read_files("txt")
  lst = count_word(dict, 6)
  lst.sort(reverse=True)
  lst = lst[:10]
  for i in lst:
    print(str(i[1]))

main()
