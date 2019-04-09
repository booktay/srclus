#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os, sys, json, requests, pprint as pp

'''
------------- Statuscode -------------
-- 3XX Series 
300 : OK
301 : A file is not found
302 : A file do not save
303 : A filename is not a json file
-- 4XX Series
400 : OK
401 : URL not response
'''

# Class for Input, Output, Request
class IORQ:
    '''
    Init
    '''
    def __init__(self):
        # print("[Init] IO")
        pass
    
    '''
    Check file path has exit
    If false, It will create a path
    ---------------- Input ---------------
    filepath = "../datas"
    --------------- Output ---------------
    Boolean(True)
    '''
    def checkpath(self, path=""):
        if os.path.exists(path):
            return True
        else:
            os.mkdir(path)
            return False

    '''
    Read Json file 
    ---------------- Input ---------------
    filepath = "../datas"
    filename = "data.json"
    --------------- Output ---------------
    list(data), int(statuscode)
    '''
    def readJson(self, filepath=".", filename=""):
        try:
            if filename.split('.')[-1] != "json" : return None, 303
            FILEPATH = os.path.join(filepath, filename)
            words = open(FILEPATH, 'r', encoding="utf-8")
            print(f'[Success] Read file at %s' % FILEPATH)
            return json.load(words), 300
        except:
            print(f'[Error] %s not found' % filename)
            return None, 301

    '''
    Write Json file 
    ---------------- Input ---------------
    filepath = "../datas"
    filename = "data.json"
    --------------- Output ---------------
    None, int(statuscode)
    '''
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

    '''
    Request a Json data from URL 
    ---------------- Input ---------------
    url = "https://www.google.co.th"
    --------------- Output ---------------
    str(data), int(statuscode)
    '''
    def requestURL(self, url=""):
        try:
            data = requests.get(url, verify=True).json()
            print(f'[Success] Request from %s' % url)
            return data, 400
        except :
            print(f'[Error] URL : %s not response' % str(url))
            return None, 401
    
    '''
    Show output to command line
    ---------------- Input ---------------
    url = "https://www.google.co.th"
    --------------- Output ---------------
    Show list on screen
    '''
    def print(self, data=None):
        pp.pprint(data)

if __name__ == "__main__":
    iorq = IORQ()
    # iorq.checkpath(path="../../test")
    # iorq.writeJson(filepath="../../test", filename="token.30010000.json")
    # iorq.readJson(filepath="../../test", filename="token.30010000.json")
    iorq.print(iorq.requestURL(url="https://ptdev03.mikelab.net/search/%E0%B8%9E%E0%B8%B1%E0%B8%99%E0%B8%97%E0%B8%B4%E0%B8%9E&page=1"))