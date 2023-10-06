import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy.io

data = {"abide":    {"control": [], "patient": []}, 
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
                    data[data_set][type].append(nx.Graph(scipy.io.loadmat(subject_path + file)["data"]))
                    break


#matrix = io.loadmat("data/abide/sub-control50030/sub-control50030_AAL116_correlation_matrix.mat")
#G = nx.Graph()
#data = pd.DataFrame(matrix["data"])
#data_filtered  = data.apply(lambda x:np.where(x==1,0,x))
#data_filtered  = data_filtered.apply(lambda x:np.where(x<0.5,0,x))
#G = nx.from_pandas_adjacency(data_filtered)
