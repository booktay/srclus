#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/preprocess module

# General Module
import os, time, re
# My Module
# from ..corpus import stopwords, customwords

class preprocess:
    def __init__(self):
        self.TIME = time.strftime("%Y-%m-%d-%H-%M")
    
    def replaceURL(self, data=""):
        TEXT = re.sub(r'([^@])(\[[a-z]*\][ ]?)?(http[s]?://)?([^ ][a-zก-ฮะ-๙0-9]+[.][a-zก-ฮะ-๙0-9]+([/&?.=\-\w]+)?)([ ]?\[/[a-z]*\])?([ ])?', r' URLLINK ', data)
        return TEXT

    def filterOnlyTHENG(self, data=""):
        TEXT = re.sub(r'[^!-~ก-๙\s]+', r'', data)
        TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
        TEXT = re.sub(r'([^a-zA-Zก-ฮ1-9๐-๙])\1{1,}', r'\1', TEXT)
        return TEXT

    def removeSpecialcharacter(self, data=""):
        TEXT = re.sub(r'[^A-Za-zก-ฮะ-๙0-9\s]+', r'', data)
        TEXT = re.sub(r'[ๆ]+', r'', TEXT)
        TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
        return TEXT

    def detectNumber(self, data=""):
        TEXT = re.sub(r'(\s)?[0-9]+(\s)?', r'', data)
        TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
        return TEXT

if __name__ == "__main__":
    pass