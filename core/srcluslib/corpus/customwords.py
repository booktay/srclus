#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/customwords module

# General Module
import os, json, sys

# Utility Module
sys.path.append('../utility')
from iorq import IORQ
IORQ = IORQ()

class Customwords:
    def __init__(self):
        pass

#     def importwords(self, filename="customwords"):
#         FILEPATH = os.path.join("srcluslib","corpus", filename + ".json")
#         if os.path.exists(FILEPATH):
#             WORDS = open(FILEPATH, 'r', encoding="utf-8")
#             return json.load(WORDS), 100
#         else: 
#             print(f'[Error] file not found at %s' % FILEPATH)
#             return None, 101

#     def target(self, customtype=None):
#         CUSTOMWORDS, STATUS = self.importwords()
#         TARGET = CUSTOMWORDS.keys() if CUSTOMWORDS else None
#         if TARGET:
#             if customtype in TARGET:
#                 return CUSTOMWORDS[customtype], 100
#             else:
#                 print(f'[Error] Please choose a type [%s]' % ','.join(x for x in self.TARGET))
#                 return None,102
#         return None, 101

# if __name__ == "__main__":
#     CUSTOMWORDS = customwords()
#     io.print("AA")
#     io.print(CUSTOMWORDS.target(customtype="tokenize"))