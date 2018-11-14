#!/usr/bin/env python
# coding: utf-8
import os
import json
from word2vec import word2vec

def openfile():
    DATA_ALL = []
    PATH_CHECK = ["token.980000.1000000.201811101445.json"]
    # PATH_CHECK = os.listdir("data")
    for one in PATH_CHECK:
        with open(os.path.join("data/", one), 'r', encoding="utf-8") as data:
            DATA_ALL = DATA_ALL + json.load(data)
    return DATA_ALL

DATA_ALL = openfile()
# print(DATA_ALL)
w2v = word2vec(DATA_ALL)
w2v.weightTfIdf()
w2v.getScore()
# print(a)

