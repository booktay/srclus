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

datas_path = os.path.join("..", "datas")
raw_datas_path = os.path.join(datas_path, "raw")
token_datas_path = os.path.join(datas_path, "token")
token_datas_path = os.path.join(token_datas_path, "newmm")
tfidf_datas_path = os.path.join(datas_path, "tfidf")
model_datas_path = os.path.join(datas_path, "model")

class procfromfile:
    def __init__(self, engine):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())
        self.ENGINE = engine

    def preparedata1(self):
        foldername = input('[Input] Folder name : ')
        datas = []
        folderpath = os.path.join(tfidf_datas_path, foldername)
        if not os.path.exists(folderpath):
            print("[Error] Can't found directory")
            return None
        resultpath = os.path.join(model_datas_path, foldername)
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
        return datas, resultpath

    def preparedata2(self):
        # Prepare data for train model
        # Don't use TF-IDF
        datas = []
        resultpath = os.path.join(model_datas_path, "newmm.all.notfidf")
        if not os.path.exists(resultpath):
            print("[Process] Create directory at " + resultpath)
            os.mkdir(resultpath)
        rootpath = token_datas_path
        folderpath = os.listdir(rootpath)
        folders = [os.path.join(rootpath, folder) for folder in folderpath]
        for folder in folders:
            for filename in os.listdir(folder):
                data, status = io.readJson(filename=filename, filepath=folder)
                data = list(data[0].values())
                if self.ENGINE == "gensim" : datas += data
                elif self.ENGINE == "tensorflow" : 
                    for line in data: datas += line
            #     break
            # break
        # io.print(datas)
        return datas, resultpath

    def run1(self, datas):
        w2v = word2vec(datas)
        print("[Initial] Initial wod2vec model")
        w2v.makeModel()
        # datas = w2v.getRawdata()
    
    def run2(self, datas, resultpath):
        print("[Initial] Initial wod2vec model")
        w2v = word2vec(resultpath=resultpath)
        print("[Process] Train wod2vec model")
        w2v.makeGensim(datas)
        print("[Complete] Train model by gensim")

    def run3(self, pathname):
        w2v = word2vec()
        w2v.loadGensim(pathname)

if __name__ == "__main__":
    # engine = input('[Input] Engine [gensim/tensorflow]: ')
    engine = "gensim"
    model = procfromfile(engine)
    datas, resultpath = model.preparedata2()
    model.run2(datas, resultpath)
    # model.run3("word.model")

