import glob
import networkx as nx

file_names_neg = glob.glob('../dataset/neg/*.txt')
file_names_pos = glob.glob('../dataset/pos/*.txt')

file_names = file_names_pos+file_names_neg
file_content = []

G = nx.Graph()

def generate_list_of_word(text):
    return text.split(" ")

def generete_list_of_edge(document_node, list_of_words):
    edges = []
    edges.append((document_node, document_node))
    for l in list_of_words:
        edges.append((document_node, l))
    return edges

for f in file_names:
    file_object = open(f, "r")
    file_content.append(file_object.readline())
    file_object.close()

G.add_nodes_from(file_names)

i = 0 

# This for implements edges from word to documents
for i in range(0,len(file_names)):
    lw = generate_list_of_word(file_content[i])
    le = generete_list_of_edge(file_names[i], lw)
    G.add_edges_from(le)


print(G.number_of_edges())
print(G.number_of_nodes())

## TODO:
# Implement edges from word to word
# Implement weights