#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os
import json
import requests
import pprint as pp


'''
------------- Status Code -------------
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
    # Init
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
    @staticmethod
    def checkpath(filepath=""):
        if os.path.exists(filepath):
            return True
        else:
            os.mkdir(filepath)
            return False

    '''
    Read Json file 
    ---------------- Input ---------------
    filepath = "../datas"
    filename = "data.json"
    --------------- Output ---------------
    list(data), int(statuscode)
    '''
    @staticmethod
    def readjson(filepath=".", filename=""):
        try:
            if filename.split('.')[-1] != "json":
                return None, 303
            path = os.path.join(filepath, filename)
            print(path)
            words = open(path, 'r', encoding="utf-8")
            print(words)
            print(f'[Success] Read file at %s' % path)
            return json.load(words), 300
        except IOError:
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
    @staticmethod
    def writejson(filepath=".", filename=None, data=None):
        path, ops = os.path.join(filepath, filename), "yes"
        if filename.split('.')[-1] != "json":
            return None, 303
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        if os.path.exists(path):
            print(f'[Error] File at %s is exists' % path)
            ops = input('[Question] Do you want to overwrite [yes/no]: ')
        if ops.lower() == "yes":
            with open(path, mode='w', encoding='utf-8') as rawdata:
                json.dump(data, rawdata, ensure_ascii=False, indent=2)
            print(f'[Complete] Save file at %s' % path)
            return None, 300
        else: 
            print(f'[Cancel] Not save' % path)
            return None, 302

    '''
    Request a Json data from URL 
    ---------------- Input ---------------
    url = "https://www.google.co.th"
    --------------- Output ---------------
    str(data), int(statuscode)
    '''
    @staticmethod
    def requesturl(url=""):
        try:
            data = requests.get(url, verify=True).json()
            print(f'[Success] Request from %s' % url)
            return data, 400
        except IOError:
            print(f'[Error] URL : %s not response' % str(url))
            return None, 401


    '''
    Show output to command line
    ---------------- Input ---------------
    url = "https://www.google.co.th"
    --------------- Output ---------------
    Show list on screen
    '''
    @staticmethod
    def print(data=None):
        pp.pprint(data)


# if __name__ == "__main__":
#     iorq = IORQ()
#     iorq.print(iorq.requesturl(url="https://ptdev03.mikelab.net/search/%E0%B8%9E%E0%B8%B1%E0%B8%99%E0%B8%97%E0%B8%B4%E0%B8%9E&page=1"))