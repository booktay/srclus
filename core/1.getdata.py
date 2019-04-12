#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 1.getdata

# General Module
import os
import sys

# My Module
# sys.path.insert(0, os.path.abspath(''))
from srcluslib.utility.iorq import IORQ
from srcluslib.corpus.pantip import Pantip
from srcluslib.model.tokenize import Tokenize

def collectPantip(io=None):
        datas = [{},{}]
        rangethread = [8000001, 8580770]
        for i in range(rangethread[0], rangethread[1] + 1):
            thread = str(3*10**7 + i)
            try:
                data, status = io.requestPantipthread(thread=thread, security=True)
                if status == 400 : 
                    datas[0] = {**datas[0], **data}
                else:
                    datas[0][thread] = ""
                    datas[1][thread] = status
                if i % 10000 == 0 or i == int(rangethread[1]):
                    io.writeJson(filename=thread+".json", filepath="datas/raw/39/", data=datas)
                    datas = [{},{}]
            except KeyboardInterrupt:
                print("[Cancel] Ctrl-c Detection")
                break
                sys.exit(0)

def checkCollectPantip(io=None):
    folderpath="../../datas"
    folders = os.listdir(folderpath)
    tempforrequest = []
    count = 0
    for folder in folders:
        filepaths = os.path.join(folderpath, folder)
        for filename in os.listdir(filepaths):
            data, status = io.readJson(filename=filename, filepath=filepaths)
            count+=1
            for name, status in data[1].items():
                # io.print([name, status])
                if status == 401:
                    tempforrequest.append(name)
    io.print([count, tempforrequest])


iorq = IORQ()
pantip = Pantip()
data = pantip.requestthread(thread="37681939")  # "35421656", "33869381"
data = list(data[0].values())[0]
tk = Tokenize()
rep, status_url = tk.replaceurl(data=data)
rep, status_f = tk.filtertheng(data=rep)
rep, status_nt = tk.numth(data=rep)
rep, status_t = tk.run(data=rep)
