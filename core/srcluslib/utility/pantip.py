# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os, sys, json, requests

# My Module
from iorq import IORQ
iorq = IORQ()

'''
------------- Statuscode -------------
-- 4XX Series
400 : OK
401 : Max retries exceeded on thread
402 : URL not response
'''

# Class for Request API from Pantip
class Pantip:
    '''
    Init
    '''
    def __init__(self):
        # print("[Init] IO Pantip")
        pass

    '''
    Request a Json thread data from Pantip 
    ---------------------------- Input --------------------------------
    Pattern = https://ptdev03.mikelab.net/kratoo/<Thread-Number>
    Thread-Number = str(31234567)
    ---------------------------- Output -------------------------------
    list(data), int(statuscode)
    '''
    def requestThread(self, thread=""):
        url = "https://ptdev03.mikelab.net/kratoo/"+ str(thread)
        try:
            data, statuscode = iorq.requestURL(url)
            # iorq.print(data)
            if statuscode == 400 and data and data['found']:
                print(f'[Success] Request from thread %s ' % thread)
                return {data['_id']: data['_source']['title'] + data['_source']['desc']}, 400
            else:
                # print(f'[Error] Thread : %s not response' % thread)
                return None, 402
        except :
            # print(f'[Error] Max retries exceeded on thread %s' % str(url))
            return None, 401

    '''
    Request a Json thread data from Pantip 
    ---------------------------- Input --------------------------------
    Pattern = https://ptdev03.mikelab.net/search/<Keyword>&page=<Pages>
    Keyword = str(apple)
    Pages = str(1)
    ---------------------------- Output -------------------------------
    list(data), int(statuscode)
    '''
    def requestSearch(self, keywords="", pages=""):
        try:
            url = "https://ptdev03.mikelab.net/search/"+ str(keywords) + "&page=" + str(pages)
            data, statuscode = iorq.requestURL(url)
            if statuscode == 400 and data and data['pts_searchResult']['hits']:
                print(f'[Success] Request from word : %s, pages : %s' % (keywords, pages))
                return data['pts_searchResult']['hits'], 400
            else:
                print(f'[Error] Thread : %s not response' % keywords)
                return None, 403
        except :
            print(f'[Error] word %s on page %s' % (keywords, pages))
            return None, 401

# if __name__ == "__main__":
    # pantip = Pantip()
    # iorq.print(pantip.requestThread(thread="30000111"))
    # iorq.print(pantip.requestSearch(keywords="apple", pages="1"))
