#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 3.model

# General Module
import os, sys, time
# My Module
from srcluslib.utility.iorq import IORQ
from srcluslib.model.word2vec import W2V
iorq = IORQ()

datas_path = os.path.join(".", "datas")
raw_datas_path = os.path.join(datas_path, "raw")
model_datas_path = os.path.join(datas_path, "model")

tfidf_datas_path = os.path.join(datas_path, "tfidf", "20190418.1627")
token_datas_path = os.path.join(datas_path, "token", "newmm")

# ------------------------------
# Please create dir before run.
# ------------------------------
resultpath = os.path.join(model_datas_path, "newmm.all.notfidf.20")


class Model:
    def __init__(self):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())

    @staticmethod
    def getdatafromengine(filepath=".", engine="", tfidf=True):
        datas = []
        for filename in sorted(os.listdir(filepath)):
            if filename in ['.DS_Store']:
                continue
            data, status = iorq.readjson(filename=filename, filepath=filepath)
            # For Gensim
            if not tfidf:
                data = list(data[0].values())

            if engine == "1": # For Gensim
                datas += data
            elif engine == "2":  # For Tensorflow
                for line in data:
                    datas += line
            # break
        # io.print(datas)
        return datas

    # TF-IDF Process
    def preparedata1(self):
        datas = []
        for filename in sorted(os.listdir(token_datas_path)):
            if filename in ['.DS_Store']:
                continue
            filepath = os.path.join(token_datas_path, filename)
            data = self.getdatafromengine(filepath=filepath, engine="1", tfidf=False)
            datas += data
            # break
        return datas

    # No TF-IDF Process
    def preparedata2(self):
        # Prepare data for train model
        # Don't use TF-IDF
        datas = []
        folderpath = os.listdir(token_datas_path)
        folders = [os.path.join(token_datas_path, folder) for folder in folderpath]
        for folder in folders:
            data = self.getdatafromengine(filepath=folder, engine="2")
            datas += data
        # io.print(datas)
        return datas

    def run1(self, datas):
        # w2v = W2V(datas)
        # print("[Initial] Initial wod2vec model")
        # w2v.makeModel()
        # datas = w2v.getRawdata()

        # For Gensim
        print("[Initial] Initial wod2vec model")
        w2v = W2V(data=[], resultpath=resultpath)
        print("[Process] Train wod2vec model")
        w2v.makeGensim(datas)
        print("[Complete] Train model by gensim")


if __name__ == "__main__":
    model = Model()
    datas = model.preparedata1()
    # print(datas)
    model.run1(datas)
