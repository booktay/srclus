#!/usr/bin/env python
# coding: utf-8
import os
import json
from word2vec import word2vec
from srcmodel import srcmodel

def openfile():
    DATA_ALL = []
    PATH_CHECK = ["token.clean.201811210859.json"]
    # PATH_CHECK = os.listdir("data/token/")
    for one in PATH_CHECK:
        with open(os.path.join("data/", one), 'r', encoding="utf-8") as data:
            DATA_ALL = DATA_ALL + json.load(data)
    return DATA_ALL

DATA_ALL = openfile()
# print(DATA_ALL)
w2v = word2vec(DATA_ALL)
# clean_word = w2v.getWordAll()
# srcmodel().createFile(DATA=clean_word, NAME="token.clean")
print("---Calculate---")
w2v.weightTfIdf()
print("---Create Rank Word---")
rank_word = w2v.getOnlyRankWord()
print("---Create Token.TfIdf File---")
srcmodel().createFile(DATA=rank_word, NAME="token.tfidf")

# w2v.getScore()
# print(a)

