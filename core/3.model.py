#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 3.model

# General Module
import os, sys, time
# My Module
from srcluslib.utility.io import io
from srcluslib.word2vec import model

class procfromfile:
    def __init__(self):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())

    def run(self, TEXT=""):
        word_all = []
        folderpath = "datas/tfidf/"
        folders = os.listdir(folderpath)
        if not folders: 
            print("[Error] Can't found directory")
            return None
        for folder in sorted(folders):
            filepaths = os.path.join(folderpath, folder)
            for filename in sorted(os.listdir(filepaths)):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                for word in data[0].values():
                    if word != [] : word_all.append(word)
                # break
            # break
        print("[Total] Read " + str(len(word_all)) + " threads")


if __name__ == "__main__":
    procfromfile().run()

