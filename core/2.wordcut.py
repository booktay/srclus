#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 1.wordcut

# General Module
import os
import sys
import time
from multiprocessing import Pool

# My Module
from srcluslib.utility.iorq import IORQ
from srcluslib.model.tokenize import Tokenize
iorq = IORQ()
tokenize = Tokenize()

# Path
datas_path = os.path.join(os.path.abspath("."), "datas")
raw_datas_path = os.path.join(datas_path, "raw")

# Token Path
token_algo = "newmm"
token_datas_path = os.path.join(datas_path, "token", token_algo)

def reqfromFile(self, foldernumber="31"):
    datas = {}
    folderpath = os.path.join(raw_datas_path, foldernumber)
    if not os.path.exists(folderpath):
        print("[Error] Can't found directory")
        return None
    filesname = sorted(os.listdir(folderpath))
    resultpath = os.path.join(token_datas_path, foldernumber)
    if not os.path.exists(resultpath): os.mkdir(resultpath)
    for filename in filesname:
        # filepaths = os.path.join(folderpath,filename)
        data, status = iorq.readjson(filepath=folderpath, filename=filename)
        datas = {**datas, **data[0]}
    # io.print([len(datas), dict(list(datas.items())[-2:])])

    datastoken = [{},{}]
    for thread, data in datas.items():
        if data != "": 
            try:
                rep, status_url = tk.replaceurl(data=data)
                rep, status_f = tk.filtertheng(data=rep)
                rep, status_nt = tk.numth(data=rep)
                rep, status_t = tk.run(data=rep)
                datastoken[0][thread] = rep
            except KeyboardInterrupt:
                print("[Cancel] Ctrl-c detection")
                sys.exit(0)
            except:
                print("Something went wrong!!!")
                datastoken[1][thread] = 700
        iorq.print(thread)
        if int(thread) % 10000 == 0:
            iorq.writejson(filename="token."+thread+".json", filepath=resultpath, data=datastoken)
            datastoken = [{},{}]
        # break
