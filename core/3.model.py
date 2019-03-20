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
    def __init__(self, engine):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())
        self.ENGINE = engine

    def preparedata(self):
        foldername = input('[Input] Folder name : ')
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
            if self.ENGINE == "gensim" : datas += data
            elif self.ENGINE == "tensorflow" : 
                for line in data:
                    datas += line
            # break
        # io.print(datas)
        return datas

    def run1(self, datas):
        w2v = word2vec(datas)
        print("[Initial] Initial wod2vec model")
        w2v.makeModel()
        # datas = w2v.getRawdata()
    
    def run2(self, datas):
        print("[Initial] Initial wod2vec model")
        w2v = word2vec()
        print("[Process] Train wod2vec model")
        w2v.makeGensim(datas)
        print("[Complete] Train model by gensim")

    def run3(self, pathname):
        w2v = word2vec()
        w2v.loadGensim(pathname)

if __name__ == "__main__":
    engine = input('[Input] Engine [gensim/tensorflow]: ')
    model = procfromfile(engine)
    datas = model.preparedata()
    model.run3("word.model")

