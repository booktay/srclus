#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 3.model

# General Module
import os, sys, time
# My Module
from srcluslib.utility.io import io
from srcluslib.model.word2vec import word2vec
io = io()

class procfromfile:
    def __init__(self):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())

    def run(self):
        foldername = input('[Input] folder name : ')
        datas = []
        folderpath = "datas/tfidf/" + foldername
        if not os.path.exists(folderpath):
            print("[Error] Can't found directory")
            return None
        resultpath = os.path.join('datas/model/', foldername)
        if not os.path.exists(resultpath):
            print("[Process] Create directory at " + resultpath)
            os.mkdir(resultpath)
        for filename in sorted(os.listdir(folderpath)):
            data, status = io.readJson(filename=filename, filepath=folderpath)
            datas += data
            break
        io.print(datas)
        w2v = word2vec(datas)
        # datass = w2v.getRawdata()

if __name__ == "__main__":
    procfromfile().run()

