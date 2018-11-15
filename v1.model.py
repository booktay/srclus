
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

from sklearn.manifold import TSNE
import matplotlib
from matplotlib import rcParams
matplotlib.rc('font', family='Garuda')
import matplotlib.pyplot as plt
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Garuda']

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

def plot(low_dim_embs, labels, filename='tsne_thai_'+ time.strftime("%Y%m%d%H%M") +'.png'):
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(30, 30))
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label, xy=(x, y), xytext=(5, 2), textcoords='offset points', ha='right', va='bottom', fontname='Garuda')
    plt.savefig(filename)
    print("[Success] Plot Graph : " + filename)