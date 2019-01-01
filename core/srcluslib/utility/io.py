#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os, json, requests, pprint as pp

class io:
    def __init__(self):
        pass

    def read(self, filename=None, filepath="."):
        path = os.path.join(filepath, filename + ".json")
        if os.path.exists(path):
            words = open(path, 'r', encoding="utf-8")
            print(f'[Success] Read file at %s complete' % path)
            return json.load(words), 500
        else: 
            print(f'[Error] File at %s not found' % path)
            return None, 501

    def write(self, filename=None, filepath=".", data=[]):
        path, ops = os.path.join(filepath, filename + ".json"), "y"
        if not os.path.exists(filepath): os.mkdir(filepath)
        if os.path.exists(path): 
            print(f'[Error] File at %s is exists' % path)
            ops = input('[Question] Do you want to overwrite [y/n]: ')
        if ops == "y": 
            with open(path, mode='w', encoding='utf-8') as rawdata:
                json.dump(data, rawdata, ensure_ascii=False, indent=2)
            print(f'[Success] Save file at %s complete' % path)
            return None, 500
        else: 
            print(f'[Cancel] File at %s not save' % path)
            return None, 502

    def requestURL(self, url="", security=True):
        try:
            data = requests.get(url, verify=security).json()
            return data, 500
        except :
            print(f'[Error] URL : %s not response' % str(url))
            return None, 503

    def print(self, data=None):
        pp.pprint(data)

if __name__ == "__main__":
    io = io()
    data = io.requestURL(url="https://ptdev03.mikelab.net/kratoo/3000000", security=False)
    if data: io.print(data)


