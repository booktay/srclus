# coding: utf-8
# author: Siwanont Sittinam
# description: utility/io module

# General Module
import os, sys, json, requests

# My Module
from .iorq import IORQ
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
            data = iorq.requestURL(url)
            if data and data['found']:
                print(f'[Success] Request from thread %s ' % thread)
                return {data['_id']: data['_source']['title'] + data['_source']['desc']}, 400
            else:
                print(f'[Error] Thread : %s not response' % thread)
                return None, 402
        except :
            print(f'[Error] Max retries exceeded on thread %s' % str(url))
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
            data = iorq.requestURL(url)
            if data and data['pts_searchResult']['hits']:
                print(f'[Success] Request from word : %s, pages : %s' % (keywords, pages))
                return data['pts_searchResult']['hits'], 400
            else:
                print(f'[Error] Thread : %s not response' % keywords)
                return None, 403
        except :
            print(f'[Error] word %s on page %s' % (keywords, pages))
            return None, 401

# # Test Write
# def collectPantip(io=None):
#     datas = [{},{}]
#     rangethread = [8000001, 8580770]
#     for i in range(rangethread[0], rangethread[1] + 1):
#         thread = str(3*10**7 + i)
#         try:
#             data, status = io.requestPantipthread(thread=thread, security=True)
#             if status == 400 : 
#                 datas[0] = {**datas[0], **data}
#             else:
#                 datas[0][thread] = ""
#                 datas[1][thread] = status
#             if i % 10000 == 0 or i == int(rangethread[1]):
#                 io.writeJson(filename=thread+".json", filepath="datas/raw/39/", data=datas)
#                 datas = [{},{}]
#         except KeyboardInterrupt:
#             print("[Cancel] Ctrl-c Detection")
#             break
#             sys.exit(0)

# def checkCollectPantip(io=None):
#     folderpath="../../datas"
#     folders = os.listdir(folderpath)
#     tempforrequest = []
#     count = 0
#     for folder in folders:
#         filepaths = os.path.join(folderpath, folder)
#         for filename in os.listdir(filepaths):
#             data, status = io.readJson(filename=filename, filepath=filepaths)
#             count+=1
#             for name, status in data[1].items():
#                 # io.print([name, status])
#                 if status == 401:
#                     tempforrequest.append(name)
#     io.print([count, tempforrequest])

# if __name__ == "__main__":
#     io = io()
    # io.readJson(filename="token.30010000.json", filepath="../../datas/process/process2/31")
    # collectPantip(io=io)
    # checkCollectPantip(io=io)
    # data, status = io.requestPantipsearch(keywords="apple", pages="1")
    # io.print(data)