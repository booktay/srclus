#!/usr/bin/env python
# coding: utf-8
import sys
import os
import json
import requests
import time
import collections
import zipfile
import itertools
import math
import random
import numpy as np
import tensorflow as tf
import deepcut as dc
from sklearn.manifold import TSNE

def buildTokenSet():
    ALL_THREAD = [[x * 10000, (x + 1) * 10000] for x in range(20)]
    # ALL_THREAD = [[x * 10, (x + 1) * 10] for x in range(10)]
    with Pool(processes=20) as pool:
        WORD_TOKEN_ALLTHREAD = pool.map(runToken, ALL_THREAD)
    return WORD_TOKEN_ALLTHREAD


def buildGraph(final_embeddings, reverse_dictionary):
    print(reverse_dictionary)
    try:
        tsne = TSNE(perplexity=50, n_components=2, init='pca', n_iter=5000, learning_rate=800)
        plot_only = 5000
        low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])
        labels = [reverse_dictionary[str(i)] for i in range(plot_only)]
        return low_dim_embs, labels
    except ImportError:
        print("Please install sklearn, matplotlib, and scipy to visualize embeddings.")
    return

def generateGraphdata():
    final_embeddings = loadFile('final_embeddings_201810182013')
    dataset = loadFile('dataset_201810182013')
    print("[Success] import dataset & final_embedding")
    low_dim_embs, labels = buildGraph(np.array(final_embeddings), dataset['reverse_dataset'])
    createFile({"low_dim_embs": low_dim_embs.tolist(), "labels": labels}, "plot")
    print("[Success] Subprocess plot ")

def plateProcess():
    # Process 1
    # WORD_TOKEN_ALLTHREAD = buildTokenSet()
    # WORD_TOKEN_ALLTHREAD = list(itertools.chain.from_iterable(WORD_TOKEN_ALLTHREAD))
    # print(WORD_TOKEN_ALLTHREAD)
    # createFile(WORD_TOKEN_ALLTHREAD, 'word_token_allthread')
    WORD_TOKEN_ALLTHREAD = loadFile('word_token_allthread_201810182013')
    print("[Complete] Process 1 : Token All thread")
    # Process 2
    buildModel(WORD_TOKEN_ALLTHREAD)
    print("[Complete] Process 2 : Model")

    def buildDataset(self, WORDS, VOCABULARY_SIZE):
        VOCABULARY_TOP_COUNT = [['UNK', -1]]
        VOCABULARY_TOP_COUNT.extend(collections.Counter(
            WORDS).most_common(VOCABULARY_SIZE - 1))
        DATASET = dict()
        for word, _ in VOCABULARY_TOP_COUNT:
            DATASET[word] = len(DATASET)
        DATA = list()
        UNKNOWN_COUNT = 0
        for word in WORDS:
            if word in DATASET:
                index = DATASET[word]
            else:
                index = 0  # DATASET['UNK']
                UNKNOWN_COUNT += 1
            DATA.append(index)
        VOCABULARY_TOP_COUNT[0][1] = UNKNOWN_COUNT
        REVERSE_DATASET = dict(zip(DATASET.values(), DATASET.keys()))
        return DATA, VOCABULARY_TOP_COUNT, DATASET, REVERSE_DATASET

    def generateBatch(self, BATCH_SIZE, SKIPS_NUM, SKIP_WINDOW, DATA, DATA_INDEX):
        assert BATCH_SIZE % SKIPS_NUM == 0
        assert SKIPS_NUM <= 2 * SKIP_WINDOW
        BATCH = np.ndarray(shape=(BATCH_SIZE), dtype=np.int32)
        LABELS = np.ndarray(shape=(BATCH_SIZE, 1), dtype=np.int32)
        SPAN = 2 * SKIP_WINDOW + 1
        BUFFER = collections.deque(maxlen=SPAN)
        for _ in range(SPAN):
            BUFFER.append(DATA[DATA_INDEX])
            DATA_INDEX = (DATA_INDEX + 1) % len(DATA)
        for i in range(BATCH_SIZE // SKIPS_NUM):
            TARGET = SKIP_WINDOW
            TARGETS_TO_AVOID = [SKIP_WINDOW]
            for j in range(SKIPS_NUM):
                while TARGET in TARGETS_TO_AVOID:
                    TARGET = random.randint(0, SPAN - 1)
                TARGETS_TO_AVOID.append(TARGET)
                BATCH[i * SKIPS_NUM + j] = BUFFER[SKIP_WINDOW]
                LABELS[i * SKIPS_NUM + j, 0] = BUFFER[TARGET]
            BUFFER.append(DATA[DATA_INDEX])
            DATA_INDEX = (DATA_INDEX + 1) % len(DATA)
        DATA_INDEX = (DATA_INDEX + len(DATA) - SPAN) % len(DATA)
        return BATCH, LABELS, DATA_INDEX

    def build(self):
        VOCABULARY_SIZE = 100000
        DATA, VOCABULARY_TOP_COUNT, DATASET, REVERSE_DATASET = self.buildDataset(
            self.WORD_TOKEN_ALLTHREAD, VOCABULARY_SIZE)
        # print(DATA, VOCABULARY_TOP_COUNT, DATASET, REVERSE_DATASET)
        createFile({"data": DATA, "vocabulary_top_count": VOCABULARY_TOP_COUNT,
                    "dataset": DATASET, "reverse_dataset": REVERSE_DATASET}, "dataset")
        del WORD_TOKEN_ALLTHREAD
        print("[Complete] Subprocess : Generate Dataset")

        # We pick a random validation set to sample nearest neighbors. Here we limit the
        # validation samples to the words that have a low numeric ID, which by
        # construction are also the most frequent.
        valid_size = 16     # Random set of words to evaluate similarity on.
        # Only pick dev samples in the head of the distribution.
        valid_window = 100
        valid_examples = np.random.choice(
            valid_window, valid_size, replace=False)
        num_sampled = 64    # Number of negative examples to sample.

        BATCH_SIZE = 128
        embedding_size = 128  # Dimension of the embedding vector.
        SKIP_WINDOW = 1       # How many words to consider left and right.
        # How many times to reuse an input to generate a label.
        SKIPS_NUM = 2

        # Init graph
        graph = tf.Graph()
        with graph.as_default():
            # Input DATA.
            train_inputs = tf.placeholder(tf.int32, shape=[BATCH_SIZE])
            train_labels = tf.placeholder(tf.int32, shape=[BATCH_SIZE, 1])
            valid_DATAset = tf.constant(valid_examples, dtype=tf.int32)

            # Ops and variables pinned to the CPU because of missing GPU implementation
            with tf.device('/cpu:0'):
                # Look up embeddings for inputs.
                embeddings = tf.Variable(tf.random_uniform(
                    [VOCABULARY_SIZE, embedding_size], -1.0, 1.0))
                embed = tf.nn.embedding_lookup(embeddings, train_inputs)
                print('embeddings', embeddings)
                print('embed', embed)

                # Construct the variables for the NCE loss
                nce_weights = tf.Variable(tf.truncated_normal(
                    [VOCABULARY_SIZE, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))
                nce_biases = tf.Variable(tf.zeros([VOCABULARY_SIZE]))
                print('nce_weights', nce_weights)
                print('nce_biases', nce_biases)

            # tf.nce_loss automatically draws a new sample of the negative labels each
            # time we evaluate the loss.
            loss = tf.reduce_mean(
                tf.nn.nce_loss(weights=nce_weights,
                               biases=nce_biases,
                               labels=train_labels,
                               inputs=embed,
                               num_sampled=num_sampled,
                               num_classes=VOCABULARY_SIZE))

            # Construct the SGD optimizer using a learning rate of 1.0.
            optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

            # Compute the cosine similarity between minibatch examples and all embeddings.
            norm = tf.sqrt(tf.reduce_sum(
                tf.square(embeddings), 1, keepdims=True))
            normalized_embeddings = embeddings / norm
            valid_embeddings = tf.nn.embedding_lookup(
                normalized_embeddings, valid_DATAset)
            similarity = tf.matmul(
                valid_embeddings, normalized_embeddings, transpose_b=True)

            # Add variable initializer.
            init = tf.global_variables_initializer()

        num_steps = 30001
        # Training
        print("[Start] Training ...")
        with tf.Session(graph=graph) as session:
            # We must initialize all variables before we use them.
            init.run()
            print("[Init] Initial Create Model Process")

            average_loss = 0
            GROUP = {}
            for step in xrange(num_steps):
                batch_inputs, batch_labels, data_index = generateBatch(
                    BATCH_SIZE, SKIPS_NUM, SKIP_WINDOW, DATA=DATA, DATA_INDEX=0)
                # print('batch_inputs = ', batch_inputs);
                # print('batch_labels = ', batch_labels);

                feed_dict = {
                    train_inputs: batch_inputs,
                    train_labels: batch_labels
                }

                # We perform one update step by evaluating the optimizer op (including it
                # in the list of returned values for session.run()
                _, loss_val = session.run(
                    [optimizer, loss], feed_dict=feed_dict)
                average_loss += loss_val

                if step % 2000 == 0:
                    if step > 0:
                        average_loss /= 2000
                    # The average loss is an estimate of the loss over the last 2000 batches.
                    print("Average loss at step ", step, ": ", average_loss)
                    average_loss = 0

                # Note that this is expensive (~20% slowdown if computed every 500 steps)
                if step % 10000 == 0:
                    sim = similarity.eval()
                    for i in xrange(valid_size):
                        valid_word = REVERSE_DATASET[valid_examples[i]]
                        top_k = 8  # number of nearest neighbors
                        nearest = (-sim[i, :]).argsort()[1:top_k + 1]
                        log_str = "Nearest to %s:" % valid_word
                        NEIGHBOR = []
                        for k in xrange(top_k):
                            close_word = REVERSE_DATASET[nearest[k]]
                            log_str = "%s %s," % (log_str, close_word)
                            NEIGHBOR.append(close_word)
                        GROUP[valid_word] = NEIGHBOR
                        print(log_str)
                # print(GROUP)
            createFile(GROUP, 'model')
            final_embeddings = normalized_embeddings.eval()
            #   print('sim = ',sim, tf.shape(sim).eval(), tf.rank(sim).eval());
            #   print('final_embeddings = ',final_embeddings, tf.shape(final_embeddings).eval(), tf.rank(final_embeddings).eval());
            createFile(final_embeddings.tolist(), 'final_embeddings')
            print("[Complete] Subprocess : Generate final_embeddings")

        low_dim_embs, labels = buildGraph(final_embeddings, REVERSE_DATASET)
        createFile({"low_dim_embs": low_dim_embs.tolist(),
                    "labels": labels}, "plot")
        print("[Success] Subprocess plot ")
