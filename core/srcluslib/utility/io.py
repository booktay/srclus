#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os, sys, json, requests, pprint as pp

class io:
    def __init__(self):
        pass

    def readJson(self, filename=None, filepath="."):
        if filename.split('.')[-1] != "json": return None, 303
        path = os.path.join(filepath, filename)
        if os.path.exists(path):
            words = open(path, 'r', encoding="utf-8")
            print(f'[Success] Read file at %s complete' % path)
            return json.load(words), 300
        else: 
            print(f'[Error] File at %s not found' % path)
            return None, 301

    def writeJson(self, filename=None, filepath=".", data=None):
        path, ops = os.path.join(filepath, filename), "yes"
        if filename.split('.')[-1] != "json": return None, 303
        if not os.path.exists(filepath): os.mkdir(filepath)
        if os.path.exists(path): 
            print(f'[Error] File at %s is exists' % path)
            ops = input('[Question] Do you want to overwrite [yes/no]: ')
        if ops.lower() == "yes": 
            with open(path, mode='w', encoding='utf-8') as rawdata:
                json.dump(data, rawdata, ensure_ascii=False, indent=2)
            print(f'[Success] Save file at %s complete' % path)
            return None, 300
        else: 
            print(f'[Cancel] File at %s not save' % path)
            return None, 302

    def requestURL(self, url="", security=True):
        try:
            data = requests.get(url, verify=security).json()
            print(f'[Success] Request from %s' % url)
            return data, 400
        except :
            print(f'[Error] URL : %s not response' % str(url))
            return None, 401

    def requestPantip(self, thread="", security=True):
        url = "https://ptdev03.mikelab.net/kratoo/"+ thread
        try:
            data = requests.get(url, verify=security).json()
            if data and data['found']:
                print(f'[Success] Request from thread %s ' % thread)
                return {data['_id']: data['_source']['title'] + data['_source']['desc']}, 400
            else:
                print(f'[Error] Thread : %s not response' % thread)
                return None, 402
        except :
            print(f'[Error] Max retries exceeded on thread %s' % str(url))
            return None, 401

    def print(self, data=None):
        pp.pprint(data)

# Test Write
def collectPantip(io=None):
    datas = [{},{}]
    for i in range(2*10**6+9*10**5+1, 2*10**6+9*10**5+1*10**4+1):
        thread = str(3*10**7 + i)
        try:
            data, status = io.requestPantip(thread=thread, security=True)
            if status == 400 : 
                datas[0] = {**datas[0], **data}
            else:
                datas[0][thread] = ""
                datas[1][thread] = status
            if i % 10000 == 0 or i == 8*10**6:
                io.writeJson(filename=thread, filepath="result/", data=datas)
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

if __name__ == "__main__":
    io = io()
    io.readJson(filename="token.30010000.json", filepath="../../datas/process/process2/31")
    # collectPantip(io=io)
    # checkCollectPantip(io=io)