import shelve
import networkx as nx
import matplotlib.pyplot as plt

shelf = shelve.open("./shelfs/ratios")
ratios = shelf["data"]
thresholds = shelf["thresholds"]
shelf.close()

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(thresholds, ratios["control"], marker="o")
ax2.plot(thresholds, ratios["patient"], marker="o")
plt.show()
