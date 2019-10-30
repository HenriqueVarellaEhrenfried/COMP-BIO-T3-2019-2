import glob
import math 
import networkx as nx
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

file_names_neg = glob.glob('../dataset/neg/0_3.txt')
file_names_pos = glob.glob('../dataset/pos/0_9.txt')

file_names = file_names_pos+file_names_neg
file_content = []

G = nx.Graph()

def generate_list_of_word(text):
    txt = text.replace("<br />", "")
    txt = txt.replace("."," ")
    txt = txt.replace("!"," ")
    txt = txt.replace("?"," ")
    txt = txt.replace("\"","")
    txt = txt.replace("\'","")
    txt = txt.replace("(","")
    txt = txt.replace(")","")

    txt = txt.lower()
    return txt.split(" ")

def generete_list_of_edge(document_node, list_of_words):
    edges = []
    edges.append((document_node, document_node))
    for l in list_of_words:
        edges.append((document_node, l))
        edges.append((l, l))
    return edges

for f in file_names:
    file_object = open(f, "r")
    file_content.append(file_object.readline())
    file_object.close()

G.add_nodes_from(file_names)

i = 0 
graph_items=[]

# This "for" implements edges and saves items
for i in range(0,len(file_names)):
    aux = {}
    lw = generate_list_of_word(file_content[i])
    le = generete_list_of_edge(file_names[i], lw)
    G.add_edges_from(le)
    aux['list_of_words'] = lw 
    aux['file_content'] = file_content[i]
    aux['file_name'] = file_names[i]
    graph_items.append(aux)

words = {}
for g in graph_items:
    
    for gl in g["list_of_words"]:
        # Get all words into Dictionary to count how many of each word exists
        if gl in words:
            words[gl]['total_count'] = words[gl]['total_count'] + 1
            if g['file_name'] in words[gl]['documents']:
                words[gl]['documents'][g['file_name']] = words[gl]['documents'][g['file_name']] + 1
            else:
                words[gl]['documents'][g['file_name']] = 1
        else:
            words[gl] = {'total_count': 1, 'documents':{g['file_name']: 1}}
# At this point, i have all the words and all occurencies by document and total


# Calculate TF-IDF
for w in words:  
    number_of_doc_with_word = len(words[w]['documents'])
    number_of_doc = len(graph_items)
    for doc in words[w]['documents']:
        freq_word_in_doc = words[w]['documents'][doc]
        tf_idf= freq_word_in_doc *  math.log10(number_of_doc/number_of_doc_with_word)    
        G.edges[w, doc]['weight'] = tf_idf


G.remove_node('')

print("Number of EDGES >> ", G.number_of_edges())
print("Number of NODES >> ", G.number_of_nodes())

nx.drawing.nx_agraph.write_dot(G,'./Dot/Test.dot')

# print(max(dict(G.degree()).items(), key = lambda x : x[1]))
# print((G.degree))
print(G.nodes(data=True))


## TODO:
# Implement weights
#   Learn how to calculate the PMI from the original article  
#       From what I learned (I need to look it deeper) I will need:
#           1) The number of times each word occurs - Let's call it function a()
#           2) The number of times word I and J are togheter - Let's call it function b()
#           4) The number of words - Let's call it function c()
#       Then I need to calculate for each edge:  log( (b(i,j)/c()) /  (a(i/c()))*(a(j)/c()) ),
#       where i is a node (word) and j is a node (word)


# dot -Tpdf Dot/Test.dot -o Dot/graph.pdf