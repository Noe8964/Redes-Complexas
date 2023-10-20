import shelve
import random
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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
                    for type in ["patient"]:
                        for usefulness in ["useful", "useless"]:
                            G = subject[type][usefulness]
                            degrees = [x[1] for x in G.degree()]
                            scaled = [x * 10 for x in degrees]
                            
                            title = f"{from_data_set} - {measure} - {type} - {usefulness} threshold of value "
                            if usefulness == "useful":
                                title += str(the_thresholds[from_data_set][measure])
                            else:
                                title += str(the_useless_thresholds[from_data_set][measures])
                                 
                            plt.title(title)
                            nx.draw(G, node_size=scaled)
                            plt.show()
                          
        del networks
                          
