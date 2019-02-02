#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 2.tfidf

# General Module
import os, sys, time
# My Module
from srcluslib.utility.io import io
from srcluslib.model.tfidf import tfidf

# Init My Module
io = io()

class procfromfile:
    def __init__(self):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())

    def run(self, TEXT=""):
        word_all = []
        folderpath = "datas/token/"
        folders = os.listdir(folderpath)
        if not folders: 
            print("[Error] Can't found directory")
            return None
        for folder in folders:
            filepaths = os.path.join(folderpath, folder)
            for filename in os.listdir(filepaths):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                for word in data[0].values():
                    if word != [] : word_all.append(word)
                # break
            # break
        print("[Total] Read " + str(len(word_all)) + " threads")
        srclustfidf = tfidf(word_all)
        response = srclustfidf.weightTfIdf()
        feature_names = srclustfidf.getFeature()
        rankword, statusrank = srclustfidf.getRank(response, feature_names)
        print("[Total] Thread ["+str(len(rankword))+"]")
        io.writeJson(filename="tfidf.all"+self.time+".json", filepath='datas/tfidf', data=rankword)

if __name__ == "__main__":
    procfromfile().run()

