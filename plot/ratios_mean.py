import shelve
import matplotlib.pyplot as plt

shelf = shelve.open("./shelfs/ratios_mean")
ratios_mean = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()

plt.plot(thresholds, ratios_mean["control"], marker="o", label="control")
plt.plot(thresholds, ratios_mean["patient"], marker="o", label="patient")
plt.legend()
plt.xlabel("threshold")
plt.ylabel("fraction of nodes in giant component")
plt.show()
