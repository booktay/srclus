#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os, sys, json, requests, pprint as pp

class IORQ:
    def __init__(self):
        # print("[Init] IO")
        pass

    def readJson(self, filepath=".", filename=""):
        if filename.split('.')[-1] != "json" : return None, 303
        FILEPATH = os.path.join(filepath, filename)
        if os.path.exists(FILEPATH):
            words = open(FILEPATH, 'r', encoding="utf-8")
            # print(f'[Success] Read file at %s complete' % FILEPATH)
            return json.load(words), 300
        else: 
            # print(f'[Error] File at %s not found' % FILEPATH)
            return None, 301

    def writeJson(self, filepath=".", filename=None, data=None):
        FILEPATH, OPS = os.path.join(filepath, filename), "yes"
        if filename.split('.')[-1] != "json": return None, 303
        if not os.path.exists(filepath): os.mkdir(filepath)
        if os.path.exists(FILEPATH) : 
            print(f'[Error] File at %s is exists' % FILEPATH)
            OPS = input('[Question] Do you want to overwrite [yes/no]: ')
        if OPS.lower() == "yes" : 
            with open(FILEPATH, mode='w', encoding='utf-8') as rawdata:
                json.dump(data, rawdata, ensure_ascii=False, indent=2)
            print(f'[Complete] Save file at %s' % FILEPATH)
            return None, 300
        else: 
            print(f'[Cancel] Not save' % FILEPATH)
            return None, 302

    def requestURL(self, url=""):
        try:
            data = requests.get(url, verify=True).json()
            # print(f'[Success] Request from %s' % url)
            return data, 400
        except :
            # print(f'[Error] URL : %s not response' % str(url))
            return None, 401

# if __name__ == "__main__":
#     io = io()
    # io.readJson(filename="token.30010000.json", filepath="../../datas/process/process2/31")
    # collectPantip(io=io)
    # checkCollectPantip(io=io)
    # data, status = io.requestPantipsearch(keywords="apple", pages="1")
    # io.print(data)