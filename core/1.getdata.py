#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 1.getdata

# General Module
import os
import sys

# My Module
from srcluslib.utility.iorq import IORQ
from srcluslib.corpus.pantip import Pantip
iorq = IORQ()
pantip = Pantip()

def collectPantip():
        datas = [{},{}]
        startthread = 38580000
        stopthread = 38758650 # Update 12/04/2562 23:50
        savepath = os.path.join(os.path.abspath("."), "datas", "raw", "39")
        for i in range(startthread, stopthread + 1):
            try:
                data, status = pantip.requestthread(thread=str(i))
                if status == 400 : 
                    datas[0] = {**datas[0], **data}
                else:
                    datas[0][str(i)] = ""
                    datas[1][str(i)] = status
                if i != startthread and (i % 10000 == 0 or i == stopthread):
                    iorq.writejson(filepath=savepath, filename=str(i)+".json", data=datas)
                    datas = [{},{}]
                    # break
            except KeyboardInterrupt:
                print("[Cancel] Ctrl-c Detection")
                sys.exit(0)

def checkCollectPantip():
    folderpath = os.path.join(os.path.abspath("."), "datas", "raw")
    folders = os.listdir(folderpath)
    tempforrequest = []
    count = 0
    for folder in folders:
        filepaths = os.path.join(folderpath, folder)
        for filename in os.listdir(filepaths):
            data, status = iorq.readjson(filepath=filepaths, filename=filename)
            count+=1
            for name, status in data[1].items():
                # io.print([name, status])
                if status == 401:
                    tempforrequest.append(name)
    iorq.print([count, tempforrequest])

collectPantip()
