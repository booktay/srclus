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
iorq = IORQ()
pantip = Pantip()


# Home
# ---------------------------
@app.route('/', methods=['GET'])
def home():
    return "<h1>Search Result Clustering</h1>"

# API
# ---------------------------
@app.route('/api', methods=['GET'])
def api():
    return "<h1>API</h1>"

# Load Model
model_path = os.path.join(os.path.abspath("."), "datas", "model", "newmm.all.notfidf", "vocab.model")
model_newmm = Word2Vec.load(model_path)

# Search Similarity Word API
# ---------------------------
# Query
# search?words=A,B,C,D,...
# ---------------------------
@app.route('/api/search/w', methods=['GET'])
def search():
    if 'words' in request.args and request.args['words'] != "":
        w = request.args['words'].split(",")
        data =  jsonify(model_newmm.most_similar(positive=w, topn=10))
        return make_response(data, 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

# Pantip Word Search
# ---------------------------
# ---------------------------
@app.route('/api/pantip/w/<word>/<int:page>', methods=['GET'])
def pantipw(word, page):
    if word and page:
        if page > 10:
            abort(404)
        data, status = pantip.requestsearch(keywords=word, pages=str(page))
        datas = []
        for i in range(len(data['hits'])):
            data_thread, status = pantip.requestthread(thread=data["hits"][i]["_id"])
            data_thread = data_thread[data["hits"][i]["_id"]]
            datas.append({
                "id": data["hits"][i]["_id"],
                "score": data["hits"][i]["_score"],
                "title": data_thread['title'],
                "desc": data_thread['desc']
            })
        return make_response(jsonify(datas), 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

# Pantip Thread Search
# ---------------------------
# ---------------------------
@app.route('/api/pantip/t/<thread>', methods=['GET'])
def pantipt(thread):
    if thread:
        data, status = pantip.requestthread(thread=thread)
        return make_response(jsonify(data), 200, {'Content-Type': 'application/json'})
    else:
        abort(404)

@app.errorhandler(404)
def not_found(e):
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)
