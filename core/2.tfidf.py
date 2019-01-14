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
        datas = {}
        folderpath = "datas/process/process" + processnumber
        folders = os.listdir(folderpath)
        for folder in folders:
            filepaths = os.path.join(folderpath, folder)
            resultpath = os.path.join('dataifidf/', folder)
            if not os.path.exists(resultpath): os.mkdir(resultpath)
            for filename in os.listdir(filepaths):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                datas = {**datas, **data[0]}
        io.print([len(datas), dict(list(datas.items())[-2:])])

        # datastfidf = [{}, {}]
        # for thread, data in datas.items():
        #     if data != "":
        #         try:
        #             # print(DATA_VALUES)
        #             srclustfidf = tfidf(data)
        #             RANK_WORD = srclustfidf.getRank()
        #             datastoken[0][thread] = text
                # except KeyboardInterrupt:
                #     print("[Cancel] Ctrl-c detection")
                #     sys.exit(0)
                # except:
                #     print("Something went wrong!!!")
        #             datastoken[0][thread] = []
        #             datastoken[1][thread] = 700
            # io.print(thread)
            # if int(thread) % 10000 == 0:
        #         io.writeJson(filename="token."+thread+".json", filepath="dataifidf/"+str(int(thread[0:2])+1)+"/", data=datastoken)
                # datastoken = [{},{}]

if __name__ == "__main__":
    procfromfile().run()

