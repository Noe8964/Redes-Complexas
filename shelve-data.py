import shelve
import scipy.io
import os
import networkx as nx
import pandas as pd
import numpy as np

data = {"abide":    {"control": [], "patient": []}, 
        "neurocon": {"control": [], "patient": []}, 
        "ppmi":     {"control": [], "patient": []}, 
        "taowu":    {"control": [], "patient": []}}

filtered_data = {"abide":    {"control": [], "patient": []}, 
                 "neurocon": {"control": [], "patient": []}, 
                 "ppmi":     {"control": [], "patient": []}, 
                 "taowu":    {"control": [], "patient": []}}

for data_set in ["abide", "neurocon", "ppmi", "taowu"]:
    for type in ["control", "patient"]:
        base_path = "./data/" + data_set + "/" + type + "/"
        for subject in os.listdir(base_path):
            subject_path = base_path + "/" + subject + "/"
            for file in os.listdir(subject_path):
                if "AAL116_correlation_matrix" in file:
                    
                    file_path = subject_path + file

                    data[data_set][type].append(nx.Graph(scipy.io.loadmat(file_path)["data"]))

                    aux = pd.DataFrame(scipy.io.loadmat(file_path)["data"])
                    aux = aux.apply(lambda x : np.where(x == 1, 0, x))
                    aux = aux.apply(lambda x : np.where(x < 0.5, 0, x))
                    filtered_data[data_set][type].append(nx.from_pandas_adjacency(aux))

                    break

file = shelve.open("shelf")
file["data"] = data
file["filtered_data"] = filtered_data
file.close()
