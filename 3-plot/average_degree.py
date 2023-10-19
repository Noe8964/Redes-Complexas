import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from_data_set = "ppmi"

shelf = shelve.open("./shelfs/average_degrees_" + from_data_set)
average_degrees = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()


n = min(len(average_degrees["control"]), len(average_degrees["patient"]))
data_frame_min = {"threshold": thresholds.tolist()*n, "control": [], "patient": []}
for type in ["control", "patient"]:
    for i in range(n):
        data_frame_min[type] += average_degrees[type][i]
df_min = pd.DataFrame(data_frame_min)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_min, x="threshold", y="control")
sns.lineplot(data=df_min, x="threshold", y="patient")
plt.savefig("./images/average_degrees/" + from_data_set + "_min" + ".png")
plt.show()


""" data_frame_control = {"threshold": thresholds.tolist()*len(average_degrees["control"]), "data": []}
data_frame_patient = {"threshold": thresholds.tolist()*len(average_degrees["patient"]), "data": []}
for i in range(len(average_degrees["control"])):
    data_frame_control["data"] += average_degrees["control"][i]
for i in range(len(average_degrees["patient"])):
    data_frame_patient["data"] += average_degrees["patient"][i]
df_control = pd.DataFrame(data_frame_control)
df_patient = pd.DataFrame(data_frame_patient)

sns.set_theme(style="darkgrid")
sns.lineplot(data=df_control, x="threshold", y="data")
sns.lineplot(data=df_patient, x="threshold", y="data")
plt.savefig("./images/average_degrees/" + from_data_set + "_nmin" + ".png")
plt.show() """
