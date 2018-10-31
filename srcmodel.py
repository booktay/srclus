# Import Basic Module
import sys
import os
import json
import requests
import time
import re
from pythainlp.tokenize import word_tokenize
from pythainlp.tag import pos_tag
from pythainlp.corpus import stopwords

class srcmodel:

    def __init__(self):
        self.TIMENOW = time.strftime("%Y%m%d%H%M")
        self.CUSTOM_STOP = self.loadCustomStopword()

    def loadFile(self, NAME=""):
        WORDS = []
        PATH = os.path.join('data/', NAME + '.json')
        with open(PATH, mode='r', encoding='utf-8') as store_word:
            WORDS = json.load(store_word)
        return WORDS

    def createFile(self, DATA=[], NAME=""):
        if not os.path.exists('data'):
            os.mkdir('data')
        with open(os.path.join('data/', NAME + "." + self.TIMENOW + '.json'), mode='x', encoding='utf-8') as store_word:
            json.dump(DATA, store_word, ensure_ascii=False)

    def loadCustomStopword(self):
        with open('custom_word.json', mode='r', encoding='utf-8') as custom_word:
            CUSTOM_WORD = json.load(custom_word)
        return CUSTOM_WORD

    def replaceWord(self, TEXT=""):
        TEXT = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', TEXT)
        TEXT = re.sub(r'[@:.\&;=$#?+{}()[\],><|!\*_"\'–·]', '', TEXT)
        TEXT = re.sub(r'[ๆ“”]', '', TEXT)
        # TEXT = re.sub(r'\s+(\d)+\s', r'\1', TEXT)
        TEXT = TEXT.strip()
        TEXT = re.split(' ', TEXT)
        return TEXT

    def tokenWord(self, TEXT=[]):
        POS_WORD = []
        try:
            for text in TEXT:
                POS_WORD += word_tokenize(text, engine='deepcut')
            #
            STOP = stopwords.words('thai')
            i = 0
            while i < len(POS_WORD):
                if POS_WORD[i] in STOP:
                    POS_WORD.remove(POS_WORD[i])
                    i -= 1
                i += 1
            #
            # print(*POS_WORD, sep=", ")
            POS_WORD = pos_tag(POS_WORD, engine='artagger', corpus='orchid')
            #
            i = 0
            while i < len(POS_WORD):
                if not POS_WORD[i][1] == "NCMN":
                    POS_WORD.remove(POS_WORD[i])
                    i -= 1
                i += 1
        except:
            print('[Error] Tokenization : ')
            print(*TEXT, sep=", ")
            return []
        return POS_WORD

    def cutPOS(self, TEXT=[]):
        WORDS = []
        for word in TEXT:
            WORDS.append(word[0])
        return WORDS

    def getTokenWordFromUrl(self, THREAD_RUN=0):
        # Define Variable
        BASE_PATH = "https://ptdev03.mikelab.net/kratoo/"
        THREAD_ID = 30000000 + THREAD_RUN
        URL = BASE_PATH + str(THREAD_ID)

        # Request
        try:
            RAW_REQUEST = requests.get(URL).json()
        except:
            print('[Error] URL Exceed : ' + str(THREAD_ID))
            return []
        
        if (RAW_REQUEST["found"]):
            RAW_SOURCE = RAW_REQUEST["_source"]
            TOKEN_TITLE = self.replaceWord(RAW_SOURCE["title"])
            TOKEN_DESC = self.replaceWord(RAW_SOURCE["desc"])
            # TOKEN_WORD = [TOKEN_TITLE + TOKEN_DESC]
            TOKEN_WORD = self.tokenWord(TOKEN_TITLE + TOKEN_DESC)
            return self.cutPOS(TOKEN_WORD)
        return []

a = []
for i in range (100090,100100, 1):
    ran = srcmodel().getTokenWordFromUrl(THREAD_RUN=i)
    if ran:
        a.append(ran)
print(a)
