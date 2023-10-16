import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wot = "ppmi"
shelf = shelve.open("./shelfs/Centrality_in_beetween_" + wot)
centrality=shelf["data"] 
shelf.close()


shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()


n = min(len(centrality["control"]), len(centrality["patient"]))
data_frame_min = {"threshold": thresholds.tolist()*n, "control": [], "patient": []}
for type in ["control", "patient"]:
    for i in range(n):
        data_frame_min[type] += centrality[type][i]
df_min = pd.DataFrame(data_frame_min)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_min, x="threshold", y="control")
sns.lineplot(data=df_min, x="threshold", y="patient")
plt.savefig("./images/Centrality/" + wot + "beetwenn_min" + ".png")
plt.show()