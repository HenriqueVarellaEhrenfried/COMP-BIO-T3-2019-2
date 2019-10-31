import glob
import math 
import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.MultiGraph()

# Read vocabulary
with open("../dataset/imdb.vocab") as f:
    vocab = [line.rstrip() for line in f]

vocab_dict = { i : {"Total":0} for i in vocab}

# Read BoW
with open("../dataset/labeledBow.feat") as f:
    raw_bag_of_words = [line.rstrip() for line in f]

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
    
"""
At this point I have:
    * All words;
    * All file names;
    * All occurencies from each word
    * All occurencies from each word in each file
"""

# Create a node for each vocabulary
G.add_nodes_from(vocab)

# Create a node for each review name
G.add_nodes_from(review_names)


# Create edges (i,i) with weight 1 for each node i
for node in (vocab + review_names):
    G.add_edge(node, node, weight=1.0)

"""
At this point I have:
    * Nodes
    * All self edges (i,i)
"""
# The above code does not work as expected. It is needed to be examined
for i in range(0, len(review_names)):
    for j in range (1, len(bag_of_words[i])):
        word = vocab[int(bag_of_words[i][j].split(":")[0])]
        G.add_edge(word,review_names[i])
        # Add edges between words in the same file
        if j > 1:
            for k in range(j-1, 0):
                previous_word = vocab[int(bag_of_words[i][k].split(":")[0])]
                G.add_edge(word, previous_word)                




# If you want to verify something use the above lines
print("Number of NODES >> ", G.number_of_nodes())
print("Number of EDGES >> ", G.number_of_edges())
print("Number of DOCS >> ", len(review_names))
print("Number of VOCAB >> ", len(vocab))

# Before code from lines 63 to 66
# Number of NODES >>  114527
# Number of EDGES >>  3571212
# Number of DOCS >>  25000
# Number of VOCAB >>  89527


# If you desire the Graviz version of the graph use the above line
nx.drawing.nx_agraph.write_dot(G,'./Dot/Test.dot')
