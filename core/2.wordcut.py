#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 2.wordcut

# General Module
import os
import sys
import time

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

def reqfromFile(foldernumber="31"):
    folderpath = os.path.join(raw_datas_path, foldernumber)
    if not os.path.exists(folderpath):
        print("[Error] Can't found directory")
        return None
    filesname = sorted(os.listdir(folderpath))
    resultpath = os.path.join(token_datas_path, foldernumber)
    if not os.path.exists(resultpath): os.mkdir(resultpath)
    
    # Init loop
    for filename in filesname:
        datastoken = [{},{}]
        # filepaths = os.path.join(folderpath,filename)
        data, status = iorq.readjson(filepath=folderpath, filename=filename)
        # iorq.print(data[0])
        for thread, dat in data[0].items():
            if dat != "": 
                data_combine = dat['title'] + " " + data['desc']
                try:
                    rep, status_url = tokenize.replaceurl(data=dat)
                    rep, status_f = tokenize.filtertheng(data=rep)
                    rep, status_nt = tokenize.numth(data=rep)
                    rep, status_t = tokenize.run(data=rep)
                    datastoken[0][thread] = rep
                except KeyboardInterrupt:
                    print("[Cancel] Ctrl-c detection")
                    sys.exit(0)
                except:
                    print("Something went wrong!!!")
                    datastoken[1][thread] = 700
            iorq.print(thread)
        iorq.writejson(filename="token."+filename, filepath=resultpath, data=datastoken)
        # break


for i in range (31,40):
    reqfromFile(foldernumber=str(i))
