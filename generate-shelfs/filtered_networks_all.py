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

shelf = shelve.open("./shelfs/all_subjects")
all_subjects = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/ratios")
thresholds = shelf["thresholds"]
shelf.close()

for data_set in ["abide", "neurocon", "ppmi", "taowu"]:
    for type in ["control", "patient"]:
        aux = pd.DataFrame(all_subjects[data_set][type])
        aux = aux.apply(lambda x : np.where(x == 1, 0, x))
        for threshold in thresholds:
            data[data_set][type].append(nx.from_pandas_adjacency(aux.apply(lambda x : np.where(x < threshold, 0, x))))

shelf = shelve.open("./shelfs/filtered_networks_all")
shelf["data"] = data
shelf.close()
