import shelve
import networkx as nx

wot = "ppmi"

shelf = shelve.open("./shelfs/filtered_networks_with_the_threshold_" + wot)
networks = shelf["data"]
shelf.close()

mean = {"abide":    {"control": 0.0, "patient": 0.0}, 
        "neurocon": {"control": 0.0, "patient": 0.0}, 
        "ppmi":     {"control": 0.0, "patient": 0.0}, 
        "taowu":    {"control": 0.0, "patient": 0.0}}

n = min(len(networks[wot]["control"]), len(networks[wot]["patient"]))

for data_set in [wot]:
    for i in range(n):
        for type in ["control", "patient"]:
            mean[data_set][type] += nx.degree_pearson_correlation_coefficient(networks[data_set][type][i])

for data_set in [wot]:
    for type in ["control", "patient"]:
        mean[data_set][type] /= n


print(mean[wot]["control"])
print(mean[wot]["patient"])