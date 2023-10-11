import shelve
import matplotlib.pyplot as plt

shelf = shelve.open("./shelfs/ratios_all")
ratios_all = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()

ratios_mean = {"control": [], "patient": []}

n = min(len(ratios_all["control"]), len(ratios_all["patient"]))

for threshold_i in range(len(thresholds)):
    sum = {"control": 0, "patient": 0}
    for subject_i in range(n):
        sum["control"] += ratios_all["control"][subject_i][threshold_i]
        sum["patient"] += ratios_all["patient"][subject_i][threshold_i]
    ratios_mean["control"].append(sum["control"] / n)
    ratios_mean["patient"].append(sum["patient"] / n)

plt.plot(thresholds, ratios_mean["control"], marker="o", label="control")
plt.plot(thresholds, ratios_mean["patient"], marker="o", label="patient")
plt.legend()
plt.xlabel("threshold")
plt.ylabel("fraction of nodes in giant component")
plt.show()
