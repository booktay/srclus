#!/usr/bin/env python
# coding: utf-8
# -------------------------
# Siwanont Sittinam
# lib/Managing Error Data
# -------------------------

# Import Basic Module
import sys, os, requests, json, time, re

class srcluserror:
    def __init__(self):
        self.TIME = time.strftime("%Y%m%d%H%M")

    def loadFile(self, PATH="", NAME=""):
        print("[Load] " + NAME + " file")
        PATHFILE = os.path.join(PATH, NAME + ".json")
        with open(PATHFILE, mode='r', encoding='utf-8') as data:
            WORDS = json.load(data)
            print("[Success] " + NAME + " file")
            return WORDS