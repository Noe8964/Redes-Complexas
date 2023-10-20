import shelve
import random
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import functools


all_data_sets = [
    "abide",
    "neurocon",
    "ppmi",
    "taowu",
]

all_measures = [
    "assortativity",
    "average_degree",
    "betweeness_centrality",
    "closeness_centrality",
    "eigen_centrality",
    "k_core",
    "ratio",
]

data_sets = [
    "neurocon",
    "ppmi",
    "taowu",
]

measures = [
    "assortativity",
    "average_degree",
    "betweeness_centrality",
    "closeness_centrality",
    "eigen_centrality",
    "k_core",
    "ratio",
]

shelf = shelve.open("./shelfs/global")
all_thresholds = shelf["thresholds"]
shelf.close()

shelf = shelve.open("./shelfs/the_thresholds")
the_thresholds = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/the_useless_thresholds")
the_useless_thresholds = shelf["data"]
shelf.close()

for from_data_set in data_sets:
        shelf = shelve.open(f"./shelfs/filtered_networks_{from_data_set}")
        networks = shelf["data"]
        shelf.close()

        for measure in measures:
            random_control_i = random.randint(0, len(networks[from_data_set]["control"])-1)
            random_patient_i = random.randint(0, len(networks[from_data_set]["patient"])-1)
            useful_i  = all_thresholds.tolist().index(the_thresholds[from_data_set][measure])
            useless_i = all_thresholds.tolist().index(the_useless_thresholds[from_data_set][measure])
            subject = {"control": {"useful":  networks[from_data_set]["control"][random_control_i][useful_i],
                                   "useless": networks[from_data_set]["control"][random_control_i][useless_i]},
                       "patient": {"useful":  networks[from_data_set]["patient"][random_patient_i][useful_i],
                                   "useless": networks[from_data_set]["patient"][random_patient_i][useless_i]}} 
            
            match measure:
                case "assortativity":
                    for type in ["control", "patient"]:
                        for usefulness in ["useful", "useless"]:
                            G = subject[type][usefulness]
                            degrees = [x[1] for x in G.degree()]
                            scaled = [x * 1 for x in degrees]
                            
                            title = f"{from_data_set} - {measure} - {type} - {usefulness} threshold of value "
                            if usefulness == "useful":
                                title += str(the_thresholds[from_data_set][measure])
                            else:
                                title += str(the_useless_thresholds[from_data_set][measure])
                                 
                            plt.title(title)
                            nx.draw(G, node_size=scaled)
                            plt.savefig(f"./graphs/{title}.png")
                            plt.close()
                case "betweeness_centrality" | "closeness_centrality" | "eigen_centrality":
                    match measure:
                        case "betweeness_centrality":
                            f = nx.betweenness_centrality
                        case "closeness_centrality":
                            f = nx.closeness_centrality
                        case "eigen_centrality":
                            f = functools.partial(nx.eigenvector_centrality, max_iter=10000)

                    for type in ["control", "patient"]:
                        for usefulness in ["useful", "useless"]:
                            G = subject[type][usefulness]
                            centrality = f(G)
                            scaled = [x * 100 for x in list(centrality.values())]
                            
                            title = f"{from_data_set} - {measure} - {type} - {usefulness} threshold of value "
                            if usefulness == "useful":
                                title += str(the_thresholds[from_data_set][measure])
                            else:
                                title += str(the_useless_thresholds[from_data_set][measure])

                            plt.title(title)
                            nx.draw(G, node_size=scaled)
                            plt.savefig(f"./graphs/{title}.png")
                            plt.close()
                case "k_core":
                    for type in ["control", "patient"]:
                        for usefulness in ["useful", "useless"]:
                            G = subject[type][usefulness]
                            max_k_core = nx.k_core(G=G, k=max(nx.core_number(G)))
                            
                            title = f"{from_data_set} - {measure} - {type} - {usefulness} threshold of value "
                            if usefulness == "useful":
                                title += str(the_thresholds[from_data_set][measure])
                            else:
                                title += str(the_useless_thresholds[from_data_set][measure])
                                 
                            plt.title(title)
                            nx.draw(G)
                            nx.draw(max_k_core, node_color="red")
                            plt.savefig(f"./graphs/{title}.png")
                            plt.close()
                case "ratio":
                    for type in ["control", "patient"]:
                        for usefulness in ["useful", "useless"]:
                            G = subject[type][usefulness]
                            giant_component = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])                            
                            
                            title = f"{from_data_set} - {measure} - {type} - {usefulness} threshold of value "
                            if usefulness == "useful":
                                title += str(the_thresholds[from_data_set][measure])
                            else:
                                title += str(the_useless_thresholds[from_data_set][measure])
                                 
                            plt.title(title)
                            nx.draw(G, node_size=5)
                            nx.draw(giant_component, node_color="red", node_size=5)
                            plt.savefig(f"./graphs/{title}.png")
                            plt.close()

                      
                          
        del networks
                          
