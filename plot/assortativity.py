import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wot = "ppmi"

shelf = shelve.open("./shelfs/assortativities_" + wot)
assortativies = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()


""" n = min(len(assortativies["control"]), len(assortativies["patient"]))
data_frame_min = {"threshold": thresholds.tolist()*n, "control": [], "patient": []}
for type in ["control", "patient"]:
    for i in range(n):
        data_frame_min[type] += assortativies[type][i]
df_min = pd.DataFrame(data_frame_min)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_min, x="threshold", y="control")
sns.lineplot(data=df_min, x="threshold", y="patient")
plt.savefig("./images/assortativies_" + wot + "_min" + ".png")
plt.show() """


data_frame_control = {"threshold": thresholds.tolist()*len(assortativies["control"]), "data": []}
data_frame_patient = {"threshold": thresholds.tolist()*len(assortativies["patient"]), "data": []}
for i in range(len(assortativies["control"])):
    data_frame_control["data"] += assortativies["control"][i]
for i in range(len(assortativies["patient"])):
    data_frame_patient["data"] += assortativies["patient"][i]
df_control = pd.DataFrame(data_frame_control)
df_patient = pd.DataFrame(data_frame_patient)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_control, x="threshold", y="data")
sns.lineplot(data=df_patient, x="threshold", y="data")
plt.savefig("./images/assortativies/" + wot + "_nmin" + ".png")
plt.show()
