#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 2.tfidf

# General Module
import os, sys, time
# My Module
from srcluslib.utility.iorq import IORQ
from srcluslib.model.tfidf import TFIDF

# Init My Module
iorq = IORQ()

datas_path = os.path.join(".", "datas")
raw_datas_path = os.path.join(datas_path, "raw")
token_datas_path = os.path.join(datas_path, "token", "newmm")
tfidf_datas_path = os.path.join(datas_path, "tfidf")

class procfromfile:
    def __init__(self):
        self.time = time.strftime("%Y%m%d.%H%M", time.localtime())

    def getdata(self):
        word_all = []
        if not os.path.exists(token_datas_path):
            print("[Error] Can't found directory")
            return None
        folders = os.listdir(token_datas_path)
        for folder in sorted(folders):
            filepaths = os.path.join(token_datas_path, folder)
            for filename in sorted(os.listdir(filepaths)):
                if filename == ".DS_Store":
                    continue
                data, status = iorq.readjson(filename=filename, filepath=filepaths)
                for word in data[0].values():
                    if word != [] : word_all.append(word)
            #     break
            # break
        return word_all

    def run(self):
        word_all = self.getdata()
        wordsize = str(len(word_all))
        print("[Total] Read " + wordsize + " threads")
        #
        srclustfidf = TFIDF(word_all)
        del word_all
        #
        response = srclustfidf.weightTfIdf()
        print("[Complete] Get Weight")
        feature_names = srclustfidf.getFeature()
        print("[Complete] Get Feature")
        rankwords, statusrank = srclustfidf.getRank(response, feature_names)
        del response, feature_names
        print("[Total] Thread ["+str(len(rankwords)) + " / " + wordsize + "]")
        #
        rankword, wordlist = [], []
        for n in range(0,len(rankwords)):
            wordlist += rankwords[n]
            rankword.append(rankwords[n])
            if (n > 0 and n % 10000 == 0) or n == len(rankwords) - 1:
                filepathtfidf = os.path.join(tfidf_datas_path, self.time)
                iorq.writejson(filename="tfidf."+ str(n) + ".json", filepath=filepathtfidf, data=rankword)
                rankword = []
        iorq.writejson(filename="tfidf.word.json", filepath=filepathtfidf, data=wordlist)

    def convert(self):
        word_all = []
        path = input("Input folder name : ")
        folderpath = os.path.join(tfidf_datas_path , path)
        del path
        if not os.path.exists(folderpath):
            print("[Error] Can't found directory")
            return None
        folders = os.listdir(folderpath)
        for filename in sorted(folders):
            data, status = iorq.readjson(filename=filename, filepath=folderpath)
            for word in data:
                if word != [] : word_all += word
            # break
        iorq.writejson(filename="tfidf.word.json", filepath=folderpath, data=word_all)


if __name__ == "__main__":
    procfromfile().run()
    # procfromfile().convert()
