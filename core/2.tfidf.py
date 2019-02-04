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
        if not os.path.exists(folderpath):
            print("[Error] Can't found directory")
            return None
        folders = os.listdir(folderpath)
        for folder in sorted(folders):
            filepaths = os.path.join(folderpath, folder)
            for filename in sorted(os.listdir(filepaths)):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                for word in data[0].values():
                    if word != [] : word_all.append(word)
                break
            break
        print("[Total] Read " + str(len(word_all)) + " threads")
        srclustfidf = tfidf(word_all)
        response = srclustfidf.weightTfIdf()
        print("[Complete] Get Weight")
        feature_names = srclustfidf.getFeature()
        print("[Complete] Get Feature")
        rankwords, statusrank = srclustfidf.getRank(response, feature_names)
        print("[Total] Thread ["+str(len(rankwords))+ " / " + str(len(word_all)) +"]")
        rankword = []
        for n in range(0,len(rankwords)):
            rankword.append(rankwords[n])
            if (n > 0 and n % 10000 == 0) or n == len(rankwords) - 1:
                io.writeJson(filename="tfidf."+ str(n) + ".json", filepath='datas/tfidf' + "/" + self.time, data=rankword)
                rankword = []

if __name__ == "__main__":
    procfromfile().run()

