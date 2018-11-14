#!/usr/bin/env python
# coding: utf-8
import os
import json
from word2vec import word2vec

def openfile():
    DATA_ALL = []
    for one in os.listdir("data"):
        with open(os.path.join("data/", one), 'r', encoding="utf-8") as data:
            DATA_ALL = DATA_ALL + json.load(data)
    return DATA_ALL

DATA_ALL = openfile()
# print(DATA_ALL)
w2v = word2vec(DATA_ALL)
w2v.weightTfIdf()
a = w2v.getScore()()
print(a)

