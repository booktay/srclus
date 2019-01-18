#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 2.tfidf

# General Module
import os
import sys
# My Module
from srcluslib.utility.io import io
from srcluslib.model.tfidf import tfidf

# Init My Module
io = io()

class procfromfile:
    def run(self, TEXT=""):
        if not os.path.exists('dataifidf/'): os.mkdir('dataifidf/')
        processnumber = input('[Input] Process number : ')
        folderpath = "datas/process/process" + processnumber
        folders = os.listdir(folderpath)
        word_all = []
        for folder in folders:
            filepaths = os.path.join(folderpath, folder)
            resultpath = os.path.join('dataifidf/', folder)
            # if not os.path.exists(resultpath): os.mkdir(resultpath)
            for filename in os.listdir(filepaths):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                for word in data[0].values():
                    word_all.append(" ".join(word))
        word_all = [word for word in word_all if word != ""]
        io.print(len(word_all))
        srclustfidf = tfidf(word_all)
        rankword, statusrank = srclustfidf.getRank()
        rankword = [word for word in rankword if word != []]
        io.print(len(rankword))
        io.writeJson(filename="tfidf.json", filepath="dataifidf/", data=rankword)

if __name__ == "__main__":
    procfromfile().run()

