#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_files():
  import xml.etree.ElementTree as ET
  dict = {}
  for event, elem in ET.iterparse("txt"):
    s = elem.text
    s = s.split()
    # print(s)
    for i in s:
      dict[i] = dict.get(i, 0) + 1

  return dict


def count_word():
  dict = read_files()
  lst = []
  for k, v in dict.items():
    if len(k) > 6:
      lst.append([v, k])
  return lst


def main():
  lst = count_word()
  lst.sort(reverse=True)
  lst = lst[:10]
  for i in lst:
    print(str(i[1]))


main()
