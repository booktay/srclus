#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: Server

# Server Module
from flask import Flask, request, jsonify, Response, abort, make_response
app = Flask(__name__)
app.config["DEBUG"] = True

# General Module
import os

# Model Module
from gensim.models import Word2Vec

# My Module
from srcluslib.utility.iorq import IORQ
from srcluslib.corpus.pantip import Pantip
from srcluslib.model.tokenize import Tokenize
iorq = IORQ()
pantip = Pantip()
tokenize = Tokenize()

# Home
# ---------------------------
@app.route('/', methods=['GET'])
def home():
    return "<h1>Search Result Clustering</h1>"

# API
# ---------------------------
@app.route('/api', methods=['GET'])
def api():
    return "<h1>SRCLUS API</h1>"

# Load Model
model_path = os.path.join(os.path.abspath("."), "datas", "model", "newmm.all.notfidf", "vocab.model")
model_newmm = Word2Vec.load(model_path)

# Search Similarity Word API
# ---------------------------
# Query 
# use "," for seperate words
# search?words=A,B,C,D,...
# ---------------------------
@app.route('/api/search/w', methods=['GET'])
def searchw():
    if 'words' in request.args and request.args['words'] != "":
        w = request.args['words'].split(",")
        data =  jsonify(model_newmm.wv.most_similar(positive=w, topn=10))
        return make_response(data, 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

# Search Clustering of Word API
# ---------------------------
# Query
# use "," for seperate words
# search?words=A,B,C,D,...
# ---------------------------

def tokenizer(data):
    rep, status_url = tokenize.replaceurl(data=data)
    rep, status_f = tokenize.filtertheng(data=rep)
    rep, status_nt = tokenize.numth(data=rep)
    rep, status_t = tokenize.run(data=rep)
    if status_t == 600:
        rep = list(filter(lambda x: x in model_newmm.wv.vocab, rep))
        if rep:
            word = model_newmm.wv.most_similar(positive=rep, topn=5)
            return [x[0] for x in word]
    return []

@app.route('/api/cluster/<word>', methods=['GET'])
def searchc(word):
    if word:
        datas = {}
        for i in range(1, 11):
            data, status_s = pantip.requestsearch(keywords=word, pages=str(i))
            if status_s == 400 and data:
                data = data['hits']
                for i in range(len(data)):
                    data_t = getdatafromthread(data[i])
                    paragraph = data_t['title'] + " " + data_t['desc']
                    paragraph = tokenizer(paragraph)
                    for j in paragraph:
                        if j in datas:
                            datas[j].append(data_t)
                        else:
                            datas[j] = [data_t]
            del paragraph
            del data
            del data_t

        datas_group = {}
        for k, v in datas.items():
            if len(v) > 1 : 
                datas_group[k] = v

        return make_response(jsonify(datas_group), 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

# Pantip Word Search
# ---------------------------
# Query
# <word> = string
# <page> = 1-10
# ---------------------------

def getdatafromthread(data):
    data_thread, status = pantip.requestthread(thread=data["_id"])
    data_thread = data_thread[data["_id"]]
    return {
        "id": data["_id"],
        "score": data["_score"],
        "title": data_thread['title'],
        "desc": data_thread['desc']
    }

@app.route('/api/pantip/w/<word>/<int:page>', methods=['GET'])
def pantipw(word, page):
    if word and page:
        if page > 10:
            abort(404)
        data, status = pantip.requestsearch(keywords=word, pages=str(page))
        if status != 400:
            abort(404)
        data, datas = data['hits'], []
        for i in range(len(data)):
            data_t = getdatafromthread(data[i])
            datas.append(data_t)
        return make_response(jsonify(datas), 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

# Pantip Thread Search
# ---------------------------
# Query
# <thread> = 38012345
# ---------------------------
@app.route('/api/pantip/t/<thread>', methods=['GET'])
def pantipt(thread):
    if thread:
        data, status = pantip.requestthread(thread=thread)
        return make_response(jsonify(data), 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

# Error 404 Handler
# ---------------------------
@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)
