#!/usr/bin/env python
# coding: utf-8
import os, json
from srcluslib.tfidf import srclustfidf

def openfile():
    DATA_ALL = []
    PATH_CHECK = os.listdir("result/token/")
    for file_s in PATH_CHECK:
        with open(os.path.join("result/token/", file_s), 'r', encoding="utf-8") as data:
            DATA_ALL = DATA_ALL + json.load(data)
    return DATA_ALL

def list2str(datas=[]):
    temp_keys = []
    temp_values = []
    for data in datas:
        temp_keys.append(int(list(data.keys())[0]))
        temp_values.append(' '.join(list(data.values())[0]))
    return temp_keys, temp_values

DATA_ALL = openfile()
print("---list2str---")
DATA_KEYS, DATA_VALUES = list2str(DATA_ALL)
# print(DATA_KEYS, DATA_VALUES)
print("---Init tfidf---")
srclustfidf = srclustfidf(DATA_VALUES)
print("---Create Rank Word---")
RANK_WORD = srclustfidf.getOnlyRankallThread()
DATA_MERGE = dict(zip(DATA_KEYS, RANK_WORD))
print("---Create Token.TfIdf File---")
srclustfidf.createFile(DATA=DATA_MERGE, PATH="result/tfidf/", NAME="tfidf")