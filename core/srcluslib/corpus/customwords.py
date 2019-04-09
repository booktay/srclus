#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/customwords module

# General Module
import os
import sys

# My Module
sys.path.insert(0, os.path.abspath('..'))
from utility.iorq import IORQ


'''
------------- Statuscode -------------
-- 1XX Series
100 : OK
101 : Not found language
'''


# Init Customwords class
class Customwords:
    # Init
    def __init__(self):
        self.iorq = IORQ()
        corpus_datas_path = os.path.join("..", "..", "datas", "corpus")
        self.words, status = self.iorq.readjson(filepath=corpus_datas_path, filename="customwords.json")

    # '''
    # Request Customwords
    # ---------------- Input ---------------
    # custom_type = "tokenize"
    # ---------------- Output --------------
    # list(data), int(Status code)
    # '''
    def target(self, custom_type=None):
        target = self.words.keys() if self.words else None
        if target:
            if custom_type in target:
                return self.words[custom_type], 100
            else:
                print(f'[Error] Please choose another type')
                return None, 102
        return None, 101


# if __name__ == "__main__":
#     cw = Customwords()
#     iorq = IORQ()
#     iorq.print(cw.target(custom_type="tokenize"))