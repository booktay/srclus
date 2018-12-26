#!/usr/bin/env python
# coding: utf-8
import os, json, time
from srcluslib.tfidf import srclustfidf
nowtime = time.strftime("%Y%m%d%H%M")

def openfile():
    DATA_ALL = []
    # PATH_CHECK = os.listdir("result/token/")
    PATH_CHECK = ["token.201811271757.7000001.7000005.json"]
    for file_s in PATH_CHECK:
        with open(os.path.join("result/token/", file_s), 'r', encoding="utf-8") as data:
            DATA_ALL = DATA_ALL + json.load(data)
    return DATA_ALL

def list2str(datas=[]):
    temp_keys = []
    temp_values = []
    for data in datas:
        temp_keys.append(int(list(data.keys())[0]))
        temp_values.append(str(list(data.values())[0]))
    return temp_keys, temp_values

DATA_ALL = openfile()
print("---list2str---")
DATA_KEYS, DATA_VALUES = list2str(DATA_ALL)
# print(DATA_VALUES)
print("---Init tfidf---")
srclustfidf = srclustfidf(DATA_VALUES)
print("---Create Rank Word---")
# RANK_WORD = srclustfidf.weightTfIdf()
# idf = srclustfidf.getIDF()
# nameme = srclustfidf.getFeature()
# print()
# DATA_MERGE = RANK_WORD.toarray().tolist()
# srclustfidf.getTFIDF()
RANK_WORD = srclustfidf.getOnlyRankallThread()
DATA_MERGE = dict(zip(DATA_KEYS, RANK_WORD))
# DATA_MERGE = dict(zip(nameme, idf))
print("---Create Token.TfIdf File---")
FILENAME = "tfidf." + nowtime + "." + "0.0"
srclustfidf.createFile(DATA=DATA_MERGE, PATH="result/tfidf/", NAME=FILENAME)