import glob
import math 
import networkx as nx
import matplotlib.pyplot as plt

LIMIT_LINES = 1500
# TODO: Finish this function
def get_number_of_times_togheter(bow, vocabulary):
    # Get Number of times that each pair of words are neighbors
    # Returns an array with all words and all ocurrencies {word:{word2: times togheter}}
    for i in range(0,len(vocabulary)):
        for document in bow:
            for word in document:
                w = word.split(":")
                if len(w) == 2:

                else:
                    continue


        word = vocab[int(bag_of_words[i][j].split(":")[0])]


# Create Graph
G = nx.Graph()

# Read vocabulary
with open("../dataset/imdb.vocab") as f:
    vocab = [line.rstrip() for line in f]

vocab_dict = { i : {"Total":0, "Occurencies": 0, "Number of Documents":0} for i in vocab}

# Read BoW
raw_bag_of_words = []
# with open("../dataset/labeledBow.feat") as f:
#     raw_bag_of_words = [line.rstrip() for line in f]

# Read the first 1500
i = 1
for line in list(open("../dataset/labeledBow.feat")):
    raw_bag_of_words.append(line.rstrip())
    i = i + 1
    if (i > LIMIT_LINES):
        break
i = 1
for line in reversed(list(open("../dataset/labeledBow.feat"))):
    raw_bag_of_words.append(line.rstrip())
    i = i + 1
    if (i > LIMIT_LINES):
        break


bag_of_words = []
review_names = []
index = 0
for rbow in raw_bag_of_words:
    aux = rbow.split(" ")
    bag_of_words.append(aux)
    review_names.append(str(index) + '_' + str(aux[0]))
    # NOTICE: aux[0] is the score the movie received
    # The following for will create a total for each word
    index = (index + 1) % 12500
    for i in range(1,len(aux)):
        splited = aux[i].split(":")
        vocab_dict[vocab[int(splited[0])]]["Total"] = vocab_dict[vocab[int(splited[0])]]["Total"] + int(splited[1])
        vocab_dict[vocab[int(splited[0])]]["Number of Documents"] = vocab_dict[vocab[int(splited[0])]]["Number of Documents"] + 1
    

# Remove useless vocabulary
useless_vocab = []
for i in vocab:
    if vocab_dict[i]["Total"] == 0:
        useless_vocab.append(i)

final_vocab = []
for v in vocab:
    if v in useless_vocab:
        continue
    else:
        final_vocab.append(v)


"""
At this point I have:
    * All words; (final_vocab)
    * All file names; (review_names)
    * All occurencies from each word (vocab_dict)
    * All occurencies from each word in each file (bag_of_words)
"""

# Create a node for each vocabulary
G.add_nodes_from(final_vocab)

# Create a node for each review name
G.add_nodes_from(review_names)


# Create edges (i,i) with weight 1 for each node i
for node in (final_vocab + review_names):
    G.add_edge(node, node, weight=1.0)

"""
At this point I have:
    * Nodes
    * All self edges (i,i)
"""

for i in range(0, len(review_names)):
    # print(i)
    for j in range (1, len(bag_of_words[i])):
        word = vocab[int(bag_of_words[i][j].split(":")[0])]
        G.add_edge(word,review_names[i])
        # Add edges between words in the same file
        if j > 1:
            for k in range(j-1, 0, -1):
                previous_word = vocab[int(bag_of_words[i][k].split(":")[0])]

                G.add_edge(word, previous_word)                


# If you want to verify something use the above lines
print("Number of NODES >> ", G.number_of_nodes())
print("Number of EDGES >> ", G.number_of_edges())
print("Number of DOCS >> ", len(review_names))
print("Number of FINAL VOCAB >> ", len(final_vocab))
print("Number of VOCAB >> ", len(vocab))


# If you desire the Graviz version of the graph use the above line
# nx.drawing.nx_agraph.write_dot(G,'./Dot/Test.dot')


# Weights in graph:
# Given nodes i and j
# If i and j are words -> PMI(i,j)
# If i is document and j is word -> TF-IDF(i,j)
# If i is j -> 1
# Else 0

# =======PMI======= #
# #W = Number of words (len(final_vocab))
# #W(i) = Number of times that i appears (vocab_dict[i]["Occurencies"])
# #W(i,j) = Number of times that i and j are neighbors ()
#___________________#
# PMI(i,j) = log(p(i,j)/p(i)/p(j))
# p(i,j) = #W(i,j)/#W
# p(i) = #W(i)/#W

# =======TF-IDF======= #
# w(i,j) = tf(i,j) * log (N/df(i))
# tf(i,j) = Number of occurences of i in j (bag_of_words)
# df(i) = Number of documents containing i ((vocab_dict[i]["Number of Documents"]))
# N = Total number of documents (review_names)