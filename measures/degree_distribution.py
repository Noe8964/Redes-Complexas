import shelve
import networkx as nx
import matplotlib.pyplot as plt

shelf = shelve.open("./shelfs/filtered_networks_with_the_threshold_abide")
subjects = shelf["data"]
shelf.close()

hist = nx.degree_histogram(subjects["abide"]["control"][0])

print(hist)

plt.hist(hist)
plt.show()
