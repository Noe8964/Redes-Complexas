import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wot = "ppmi"

shelf = shelve.open("./shelfs/max_k_core_sizes_" + wot)
k_core = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()


""" n = min(len(k_core["control"]), len(k_core["patient"]))
data_frame_min = {"threshold": thresholds.tolist()*n, "control": [], "patient": []}
for type in ["control", "patient"]:
    for i in range(n):
        data_frame_min[type] += k_core[type][i]
df_min = pd.DataFrame(data_frame_min)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_min, x="threshold", y="control")
sns.lineplot(data=df_min, x="threshold", y="patient")
plt.savefig("./images/k_core/" + wot + "_min" + ".png")
plt.show() """


data_frame_control = {"threshold": thresholds.tolist()*len(k_core["control"]), "data": []}
data_frame_patient = {"threshold": thresholds.tolist()*len(k_core["patient"]), "data": []}
for i in range(len(k_core["control"])):
    data_frame_control["data"] += k_core["control"][i]
for i in range(len(k_core["patient"])):
    data_frame_patient["data"] += k_core["patient"][i]
df_control = pd.DataFrame(data_frame_control)
df_patient = pd.DataFrame(data_frame_patient)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_control, x="threshold", y="data")
sns.lineplot(data=df_patient, x="threshold", y="data")
plt.savefig("./images/k_core/" + wot + "_nmin" + ".png")
plt.show()
