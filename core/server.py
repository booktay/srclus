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
import operator

# Model Module
from gensim.models import Word2Vec

# My Module
from srcluslib.utility.iorq import IORQ
from srcluslib.corpus.pantip import Pantip
from srcluslib.model.tokenize import Tokenize
iorq = IORQ()
pantip = Pantip()
tokenize = Tokenize()

# app = Flask(__name__, static_folder="../websrclus/build/static", template_folder="../websrclus/build")

# @app.route("/")
# def index():
#     return render_template("index.html")

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
model_path = os.path.join(os.path.abspath("."), "datas", "model", "newmm", "vocab.model")
model_newmm = Word2Vec.load(model_path)
model_path_tfidf = os.path.join(os.path.abspath("."), "datas", "model", "newmm.tfidf", "vocab.model")
model_newmm_tfidf = Word2Vec.load(model_path_tfidf)

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

def tokenizer(data, tfidf):
    rep, status_url = tokenize.replaceurl(data=data)
    rep, status_f = tokenize.filtertheng(data=rep)
    rep, status_nt = tokenize.numth(data=rep)
    rep, status_t = tokenize.run(data=rep)
    if status_t == 600:
        if tfidf:
            rep = list(filter(lambda x: x in model_newmm_tfidf.wv.vocab, rep))
            if rep:
                word = model_newmm_tfidf.wv.most_similar(positive=rep, topn=10) #most_similar_cosmul
                return word # [x[0] for x in word]
        else:
            rep = list(filter(lambda x: x in model_newmm.wv.vocab, rep))
            if rep:
                word = model_newmm.wv.most_similar(positive=rep, topn=10)  #most_similar_cosmul
                return word # [x[0] for x in word]
    return []

@app.route('/api/cluster/<word>', methods=['GET'])
def searchc(word):
    if word:
        datas, rank = {}, {}
        tfidf = request.args.get('tfidf', default = False, type = bool)
        for i in range(1, 101):
            # print(tfidf)
            data, status_s = pantip.requestsearch(keywords=word, pages=str(i))
            if status_s == 400 and data:
                data = data['hits']
                if not data: break
                for i in range(len(data)):
                    data_t = getdatafromthread(data[i])
                    paragraph = data_t['title'] + " " + data_t['desc']
                    paragraph = tokenizer(paragraph, tfidf)
                    for j in paragraph:
                        data_score = {
                            'id' : data_t['id'],
                            'title' : data_t['title'],
                            'desc' : data_t['desc'],
                            'score' : [data_t['score']/100, j[1]]
                        }

                        score_label = data_score['score'][0] * data_score['score'][1]

                        if not j[0] in datas:
                            datas[j[0]] = [data_score]
                            rank[j[0]] = [1, score_label / 1]
                        else:
                            len_datas = len(datas[j[0]])
                            rank[j[0]]= [rank[j[0]][0] + 1,(score_label + (rank[j[0]][1] * len_datas)) / (len_datas + 1)]
                            datas[j[0]].append(data_score)

                    del paragraph, data_score
            else :
                break

        del data

        datas_group = {
            "rank": sorted(rank.items(), key=lambda e: e[1][0], reverse=True),
            "datas": datas
        }

        del rank, datas

        # iorq.writejson(filepath="../client/public/datas", filename=word+".json", data=datas_group)
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
    app.run(host='0.0.0.0', debug=True, port=5000)
