import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

all_measures = [
    "assortativity",
    "average_degree",
    "betweeness_centrality",
    "closeness_centrality",
    "eigen_centrality",
    "k_core",
    "ratio",
]

measures = [
    "assortativity",
    "average_degree",
    "betweeness_centrality",
    "closeness_centrality",
    "eigen_centrality",
    "k_core",
    "ratio",
]

for from_data_set in ["abide", "ppmi"]:
    for measure in measures:
        for subjects_min in ["min", "nmin"]:
            shelf = shelve.open("./shelfs/df_ratios_" + subjects_min + "_" + from_data_set)
            df = shelf["data"]
            shelf.close()

            the_threshold = 0.4
            for type in ["control", "patient"]:
                df[type] = df[type][df[type].threshold == the_threshold]
                del df[type]["threshold"]

            value_counts = {"control": df["control"].value_counts().sort_index(),
                            "patient": df["patient"].value_counts().sort_index()}

            to_plot = {"control": {"x": value_counts["control"].index.get_level_values(0).values,
                                   "y": value_counts["control"].values.astype("float64")},
                       "patient": {"x": value_counts["patient"].index.get_level_values(0).values,
                                   "y": value_counts["patient"].values.astype("float64")}}

            n = 30

            for type in ["control", "patient"]:
                for i in range(to_plot[type]["y"].size):
                    to_plot[type]["y"][i] /= n

            plt.plot(to_plot["control"]["x"], to_plot["control"]["y"], label="control")
            plt.plot(to_plot["patient"]["x"], to_plot["patient"]["y"], label="patient")
            plt.legend()
            plt.title("ppmi")
            plt.xlabel("fraction of giant component")
            plt.ylabel("probability of being control or patient")
            plt.show()

            shelf = shelve.open("./shelfs/probability_" + from_data_set + "_ratios")
            shelf["data"] = to_plot
            shelf.close()
