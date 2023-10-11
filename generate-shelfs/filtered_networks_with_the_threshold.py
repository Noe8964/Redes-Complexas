import shelve
import scipy.io
import networkx as nx
import pandas as pd
import numpy as np
import os

data = {"abide":    {"control": [], "patient": []}, 
        "neurocon": {"control": [], "patient": []}, 
        "ppmi":     {"control": [], "patient": []}, 
        "taowu":    {"control": [], "patient": []}}

shelf = shelve.open("./shelfs/global")
the_threshold = shelf["the_threshold"]
shelf.close()

for data_set in ["abide"]:
    for type in ["control", "patient"]:
        base_path = "./data/" + data_set + "/" + type + "/"
        for subject in os.listdir(base_path):
            subject_path = base_path + "/" + subject + "/"
            for file in os.listdir(subject_path):
                if "AAL116_correlation_matrix" in file:
                    aux = pd.DataFrame(scipy.io.loadmat(subject_path + file)["data"])
                    aux = aux.apply(lambda x : np.where(x == 1, 0, x))
                    data[data_set][type].append(nx.from_pandas_adjacency(aux.apply(lambda x : np.where(x < the_threshold, 0, x))))
                    break

shelf = shelve.open("./shelfs/filtered_networks_with_the_threshold_abide")
shelf["data"] = data
shelf.close()
