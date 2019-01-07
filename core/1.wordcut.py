#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: 1.wordcut

# General Module
import os, sys, time
from multiprocessing import Pool
# My Module
from srcluslib.utility.io import io
from srcluslib.model.preprocess import preprocess
from srcluslib.model.tokenize import tokenize
# Init My Module
preprocess = preprocess()
io = io()

def preprocessdata(word=""):
    status = [0,0,0,0,0]
    procdata = word
    procdata, status[0] = preprocess.replaceURL(data=word)
    procdata, status[1] = preprocess.filterTHENG(data=procdata)
    texts = [word for word in procdata.split(' ') if word not in ['', ' ']]
    procdata, status[3] = tokenize(data=texts).run()
    procdata, status[4] = preprocess.removeStopword(procdata)
    return procdata, status

class reqfromURL:
    def processpantipthread(self, ALL_THREAD=[1, 1, 2]):
        # a,b = input('[Input] Generate Thread Range : ').split(',')
        process = ALL_THREAD[0]
        a,b = 3*10**7 + ALL_THREAD[1], 3*10**7 + ALL_THREAD[2]
        datathread = [{},{}]
        try:
            for i in range(int(a), int(b)+1):
                io.print(f'[Process %s] thread : %s' % (str(process), str(i)))
                url = "https://ptdev03.mikelab.net/kratoo/"+ str(i)
                # Request URL
                data, statusrequest = io.requestURL(url=url, security=True)
                if statusrequest == 500:
                    if data and data['found'] : 
                        word = data['_source']['title'] + " " + data['_source']['desc']
                        # processword, statuspreprocess = preprocessdata(word=word)
                        # processword = ' '.join(processword)
                        datathread[0][data['_id']] = processword
                        # datathread[1][i] = statuspreprocess
                        io.print(word)
                    else : 
                        datathread[1][i] = statusrequest
                        io.print(f'[Error] No data at %s' % url)
            # io.print(datathread)
            # filename="token." + str(a) + "-" + str(b) # "." + time.strftime("%Y-%m-%d-%H-%M")
            # io.write(filename=filename, filepath="result/", data=datathread)
        except KeyboardInterrupt:
            io.print("[Cancel] Ctrl-C from user")

    def poolpantipthread(self):
        try :
            ALL_THREAD = []
            for i in range(1, 5):
                THREAD_MIN, THREAD_MAX = input("[Process " + str(i) +"] Thread Range [min,max]: ").split(',')
                ALL_THREAD.append([i, int(THREAD_MIN), int(THREAD_MAX)])
            with Pool(processes=4) as pool:
                pool.map(processpantipthread, ALL_THREAD)
            print("[Success] "+ str(4) + " processes")
        except KeyboardInterrupt:
            print("[Cancel] Ctrl-c Detection at createPool()")
            sys.exit(0)

class reqfromFile:
    def checkdata(self):
        folderpath="datas"
        folders = os.listdir(folderpath)
        datas = [{},{}]
        for folder in folders:
            filepaths = os.path.join(folderpath, folder)
            for filename in os.listdir(filepaths):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                for thread, data in data[0].items():
                    if data != "": 
                        try:
                            text, status = preprocessdata(data)
                            datas[0][thread] = text
                        except:
                            print("Something went wrong!!!")
                            datas[0][thread] = []
                            datas[1][thread] = 700
                        # break
                    io.print(thread)
                io.writeJson(filename="testcutall."+filename, filepath="datastest/"+folder+"/", data=datas)
                # break
            # break

if __name__ == "__main__":
    # processpantipthread(ALL_THREAD=[1,100000,100010])
    # poolpantipthread()
    reqfromFile().checkdata()