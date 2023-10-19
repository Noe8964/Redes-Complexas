import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wot = "ppmi"
_min = "min"

shelf = shelve.open("./shelfs/ratios_" + wot)
ratios = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()

if _min == "min":
    n = min(len(ratios["control"]), len(ratios["patient"]))

    data_frame_creator = {"control": {"threshold": thresholds.tolist()*n, "data": []},
                          "patient": {"threshold": thresholds.tolist()*n, "data": []}}
    
    for type in ["control", "patient"]:
        for i in range(n):
            data_frame_creator[type]["data"] += ratios[type][i]
else:
    data_frame_creator = {"control": {"threshold": thresholds.tolist()*len(ratios["control"]), "data": []},
                          "patient": {"threshold": thresholds.tolist()*len(ratios["patient"]), "data": []}}
    
    for type in ["control", "patient"]:
        for i in range(len(ratios[type])):
            data_frame_creator[type]["data"] += ratios[type][i]

df = {"control": pd.DataFrame(data_frame_creator["control"]),
      "patient": pd.DataFrame(data_frame_creator["patient"])}

sns.set_theme(style="darkgrid")
sns.lineplot(data=df["control"], x="threshold", y="data")
sns.lineplot(data=df["patient"], x="threshold", y="data")
plt.savefig("./images/ratios/" + wot + "_" + _min + ".png")
plt.show()

shelf = shelve.open("./shelfs/data_frame_ratios_" + _min + "_" + wot)
shelf["data"] = df
shelf.close()

