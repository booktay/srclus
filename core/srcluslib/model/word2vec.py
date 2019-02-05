#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/word2vec module

# Import Basic Module
import collections, time, json, os
import numpy as np
import tensorflow as tf

class word2vec:
    def __init__(self, data=[]):
        self.WORDSALL = data

    def getRawdata(self):
        return self.WORDSALL

    def getVocabulary(self):
        words = []
        for word in self.WORDSALL:
            words += word
        return set(words)

    def makeOnehot(self, words):
        word2int = {}
        int2word = {}
        vocab_size = len(words)
        for i,word in enumerate(words):
            word2int[word] = i
            int2word[i] = word
        return word2int, int2word, vocab_size 

    def toOnehot(self, data_point_index, vocab_size):
        temp = np.zeros(vocab_size)
        temp[data_point_index] = 1
        return temp

    def makeModel(self):
        vocabs = self.getVocabulary()
        print("[Process] Get Vocabulary")
        word2int, int2word, vocab_size = self.makeOnehot(vocabs)
        print("[Process] Make One-hot vector")
        WINDOW_SIZE = 2
        print("[Process] Window size : " + WINDOW_SIZE)
        data = []
        sentences = self.WORDSALL
        for sentence in sentences:
            for word_index, word in enumerate(sentence):
                for nb_word in sentence[max(word_index - WINDOW_SIZE, 0) : min(word_index + WINDOW_SIZE, len(sentence)) + 1] : 
                    if nb_word != word:
                        data.append([word, nb_word])
        
        print("[Process] Init Model")
        x_train = [] 
        y_train = [] 
        for data_word in data:
            x_train.append(self.toOnehot(word2int[data_word[0]], vocab_size))
            y_train.append(self.toOnehot(word2int[data_word[1]], vocab_size))
        
        x_train = np.asarray(x_train)
        y_train = np.asarray(y_train)
        # print(x_train.shape, y_train.shape)

        print("[Process] Init Tensorflow process")

        x = tf.placeholder(tf.float32, shape=(None, vocab_size))
        y_label = tf.placeholder(tf.float32, shape=(None, vocab_size))
        EMBEDDING_DIM = 5 
        print("[Process] Embedding dimension : " + EMBEDDING_DIM)

        W1 = tf.Variable(tf.random_normal([vocab_size, EMBEDDING_DIM]))
        b1 = tf.Variable(tf.random_normal([EMBEDDING_DIM]))
        hidden_representation = tf.add(tf.matmul(x,W1), b1)

        W2 = tf.Variable(tf.random_normal([EMBEDDING_DIM, vocab_size]))
        b2 = tf.Variable(tf.random_normal([vocab_size]))
        prediction = tf.nn.softmax(tf.add( tf.matmul(hidden_representation, W2), b2))

        print("[Process] Start Tensorflow session")

        sess = tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init) 

        print("[Process] Gradient Descent Optimizing")
        # define the loss function:
        cross_entropy_loss = tf.reduce_mean(-tf.reduce_sum(y_label * tf.log(prediction), reduction_indices=[1]))
        # define the training step:
        train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy_loss)
        n_iters = 10000
        # train for n_iter iterations
        for _ in range(n_iters):
            sess.run(train_step, feed_dict={x: x_train, y_label: y_train})
            print('loss is : ', sess.run(cross_entropy_loss, feed_dict={x: x_train, y_label: y_train}))

        print(sess.run(W1))
        print(sess.run(b1))

        print("[Process] Generate Model")
        vectors = sess.run(W1 + b1)
        # print(vectors[word2int['queen']])
        print("[Complete] Testing")
        wordtest = input('[Test] Input word : ')
        print(int2word[self.find_closest(word2int[wordtest], vectors)])
    
    def euclideandist(self, vec1, vec2):
        return np.sqrt(np.sum((vec1-vec2)**2))

    def findclosest(self, word_index, vectors):
        min_dist = 10000  # to act like positive infinity
        min_index = -1
        query_vector = vectors[word_index]
        for index, vector in enumerate(vectors):
            if self.euclidean_dist(vector, query_vector) < min_dist and not np.array_equal(vector, query_vector):
                min_dist = self.euclidean_dist(vector, query_vector)
                min_index = index
        return min_index
