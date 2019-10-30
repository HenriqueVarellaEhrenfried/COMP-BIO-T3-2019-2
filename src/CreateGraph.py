import glob
import math 
import networkx as nx
import matplotlib.pyplot as plt
import spacy

# Import english tokenizer
nlp = spacy.load('en_core_web_sm')

# Create Graph
G = nx.Graph()

# Read vocabulary
with open("../dataset/imdb.vocab") as f:
    vocab = [line.rstrip() for line in f]

vocab_dict = { i : {} for i in vocab}

# Get all file names
file_names_neg = glob.glob('../dataset/neg/*.txt')
file_names_pos = glob.glob('../dataset/pos/*.txt')
file_names = file_names_pos + file_names_neg

# Create a node for each vocabulary
G.add_nodes_from(vocab)

# Create a node for each file name
G.add_nodes_from(file_names)


# Create edges (i,i) with weight 1 for each node i
for node in vocab + file_names:
    G.add_edge(node, node, weight=1.0)


"""
So far I created the graph, added all words and all files in it and 
added the self edge (i,i)
"""

# Open each file and get each word and create its metrics



# If you want to verify something use the above lines
# print("Number of NODES >> ", G.number_of_nodes())
# print("Number of EDGES >> ", G.number_of_edges())
# print("Number of DOCS >> ", len(file_names))
# print("Number of VOCAB >> ", len(vocab))


# If you desire the Graviz version of the graph use the above line
# nx.drawing.nx_agraph.write_dot(G,'./Dot/Test.dot')
