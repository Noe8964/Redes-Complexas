import shelve
import networkx as nx
import matplotlib.pyplot as plt

hists_mean = {"ppmi": {"control": [0]*117, "patient": [0]*117}}

shelf = shelve.open("./shelfs/abide_degree_distribution_hists")
hists = shelf["data"]
shelf.close()

n = min(len(hists["ppmi"]["control"]), len(hists["ppmi"]["patient"]))

for data_set in ["ppmi"]:
    for type in ["control", "patient"]:
        for subject in range(n):
            for bin in range(len(hists[data_set][type][subject])):
                hists_mean[data_set][type][bin] += hists[data_set][type][subject][bin]

for data_set in ["ppmi"]:
    for type in ["control", "patient"]:
        for bin in range(117):
            hists_mean[data_set][type][bin] /= n

plt.hist(hists_mean["ppmi"]["control"], label="control")
plt.hist(hists_mean["ppmi"]["patient"], label="patient")
plt.legend()
plt.show()
