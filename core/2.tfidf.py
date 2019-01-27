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
                    word_all.append(" ".join(word))
        print("[Total] Remove empty thread ["+str(len(word_all))+" --> ", end="")
        word_all = [word for word in word_all if word != ""]
        print(str(len(word_all))+"]")
        srclustfidf = tfidf(word_all)
        rankword, statusrank = srclustfidf.getRank()
        rankword = [word for word in rankword if word != []]
        print("[Total] Thread ["+str(len(rankword))+"]")
        io.writeJson(filename="tfidf."+self.time+".json", filepath='datas/', data=rankword)

if __name__ == "__main__":
    procfromfile().run()

