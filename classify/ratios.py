import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


wot = "ppmi"
_min = "min"

shelf = shelve.open("./shelfs/data_frame_ratios_" + _min + "_" + wot)
df = shelf["data"]
shelf.close()

the_threshold = 0.4

for type in ["control", "patient"]:
    df[type] = df[type][df[type].threshold == the_threshold]
    del df[type]["threshold"]

value_counts = {"control": df["control"].value_counts().sort_index(),
                "patient": df["patient"].value_counts().sort_index()}

to_plot = {"control": {"x": value_counts["control"].index.get_level_values(0).values, "y": value_counts["control"].values.astype("float64")},
           "patient": {"x": value_counts["patient"].index.get_level_values(0).values, "y": value_counts["patient"].values.astype("float64")}}

#print(value_counts["control"])
#print()
#print(value_counts["patient"].index.get_level_values(0).values)
#print(value_counts["patient"].values)

n = 30

for type in ["control", "patient"]:
    for i in range(to_plot[type]["y"].size):
        print(to_plot[type]["y"][i]/n)
        to_plot[type]["y"][i] /= n

plt.plot(to_plot["control"]["x"], to_plot["control"]["y"])
plt.plot(to_plot["patient"]["x"], to_plot["patient"]["y"])
plt.show()


#sns.set_theme(style="darkgrid")
#sns.lineplot(data=df["control"].value_counts())
#sns.lineplot(data=df["patient"].value_counts())
#plt.savefig("./images/classify/" + wot + "_n_min" + ".png")
#plt.show()
