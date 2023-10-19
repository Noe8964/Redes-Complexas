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
thresholds = shelf["thresholds"]
shelf.close()

from_data_set = "ppmi"

control = ["control"]
patient = ["patient"]
both    = ["control", "patient"]

for data_set in [from_data_set]:
    for type in both:
        base_path = "./data/" + data_set + "/" + type + "/"
        for subject in os.listdir(base_path):
            subject_path = base_path + "/" + subject + "/"
            for file in os.listdir(subject_path):
                if "AAL116_correlation_matrix" in file:
                    aux = pd.DataFrame(scipy.io.loadmat(subject_path + file)["data"])
                    aux = aux.apply(lambda x : np.where(x == 1, 0, x))
                    subject_filtered_networks = []
                    for threshold in thresholds:
                        subject_filtered_networks.append(nx.from_pandas_adjacency(aux.apply(lambda x : np.where(x < threshold, 0, x))))
                    data[data_set][type].append(subject_filtered_networks)
                    del aux
                    break

shelf = shelve.open("./shelfs/filtered_networks_" + from_data_set)
shelf["data"] = data
shelf.close()
