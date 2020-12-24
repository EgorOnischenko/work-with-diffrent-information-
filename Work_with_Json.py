#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

with open('text') as f:
  json_data = json.load(f)


all_items = json_data['rss']['channel']['items']

news_list_json = []
for i in all_items:
  news_list_json.append(i['description'].split())

words_list_json = []

for i in news_list_json:
  for j in i:
    if len(j)>6:
     words_list_json.append(j)

words_set_json = set(words_list_json)

my_dict_json = {i:words_list_json.count(i) for i in words_set_json}

pairs_list_json = []

for k,v in zip(my_dict_json.keys(), my_dict_json.values()):
  pairs_list_json.append((v,k))

words_list_sorted_json = sorted(pairs_list_json, reverse=True)

for i in range(10):
  print(words_list_sorted_json[i][1])

