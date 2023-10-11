import shelve
import networkx as nx
import matplotlib.pyplot as plt

data = {"abide":    {"control": [], "patient": []}, 
        "neurocon": {"control": [], "patient": []}, 
        "ppmi":     {"control": [], "patient": []}, 
        "taowu":    {"control": [], "patient": []}}

shelf = shelve.open("./shelfs/filtered_networks_with_the_threshold_abide")
subjects = shelf["data"]
shelf.close()

for data_set in ["ppmi"]:
    for type in ["control", "patient"]:
        for network in subjects[data_set][type]:
            data[data_set][type].append(nx.degree_histogram(network))

shelf = shelve.open("./shelfs/abide_degree_distribution_hists")
shelf["data"] = data
shelf.close()
