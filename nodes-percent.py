import shelve
import networkx as nx
import matplotlib.pyplot as plt

shelf = shelve.open("shelf");
data = shelf["data"]
filtered_data = shelf["filtered_data"]
shelf.close()

subject = data["abide"]["control"][0]
filtered_subject = filtered_data["abide"]["control"][0]

subject_gcc = subject.subgraph(sorted(nx.connected_components(subject), key=len, reverse=True)[0])
filtered_subject_gcc = filtered_subject.subgraph(sorted(nx.connected_components(filtered_subject), key=len, reverse=True)[0])

print(len(filtered_subject_gcc.nodes())/len(filtered_subject.nodes()))
