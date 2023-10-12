import shelve
import scipy.io
import os
import networkx as nx

data = {"abide":    {"control": [], "patient": []}, 
        "neurocon": {"control": [], "patient": []}, 
        "ppmi":     {"control": [], "patient": []}, 
        "taowu":    {"control": [], "patient": []}}

for data_set in ["abide"]:
    for type in ["control", "patient"]:
        base_path = "./data/" + data_set + "/" + type + "/"
        for subject in os.listdir(base_path):
            subject_path = base_path + "/" + subject + "/"
            for file in os.listdir(subject_path):
                if "AAL116_correlation_matrix" in file:
                    data[data_set][type].append(nx.Graph(scipy.io.loadmat(subject_path + file)["data"]))
                    break

file = shelve.open("./shelfs/abide_networks")
file["data"] = data
file.close()
