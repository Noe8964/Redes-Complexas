import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wot = "ppmi"

shelf = shelve.open("./shelfs/ratios_" + wot)
ratios = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()

n = min(len(ratios["control"]), len(ratios["patient"]))

data_frame = {"threshold": thresholds.tolist()*n, "control": [], "patient": []}

for type in ["control", "patient"]:
    for i in range(n):
        data_frame[type] += ratios[type][i]

print(len(data_frame["threshold"]))
print(len(data_frame["control"]))
print(len(data_frame["patient"]))

df = pd.DataFrame(data_frame)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df, x="threshold", y="control")
sns.lineplot(data=df, x="threshold", y="patient")
plt.show()

#plt.plot(thresholds, ratios["control"][0], marker="o", label="control")
#plt.plot(thresholds, ratios["patient"][0], marker="o", label="patient")
#plt.legend()
#plt.xlabel("threshold")
#plt.ylabel("fraction of nodes in giant component")
#plt.title("ratios_" + wot)
#plt.savefig("./images/ratios_" + wot + ".png")
#plt.show()
