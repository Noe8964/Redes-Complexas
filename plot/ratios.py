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


""" n = min(len(ratios["control"]), len(ratios["patient"]))
data_frame_min = {"threshold": thresholds.tolist()*n, "control": [], "patient": []}
for type in ["control", "patient"]:
    for i in range(n):
        data_frame_min[type] += ratios[type][i]
df_min = pd.DataFrame(data_frame_min)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_min, x="threshold", y="control")
sns.lineplot(data=df_min, x="threshold", y="patient")
plt.savefig("./images/ratios/" + wot + "_min" + ".png")
plt.show() """


data_frame_creator = {"control": {"threshold": thresholds.tolist()*len(ratios["control"]), "data": []},
                      "patient": {"threshold": thresholds.tolist()*len(ratios["patient"]), "data": []}} 

for type in ["control", "patient"]:
    for i in range(len(ratios[type])):
        data_frame_creator[type]["data"] += ratios[type][i]
    
data_frame = {"control": pd.DataFrame(data_frame_creator["control"]),
              "patient": pd.DataFrame(data_frame_creator["patient"])}

sns.set_theme(style="darkgrid")
sns.lineplot(data=data_frame["control"], x="threshold", y="data")
sns.lineplot(data=data_frame["patient"], x="threshold", y="data")
plt.savefig("./images/ratios/" + wot + "_nmin" + ".png")
plt.show()

shelf = shelve.open("./shelfs/data_frame_ratios_" + wot)
shelf["data"] = data_frame
shelf.close()
