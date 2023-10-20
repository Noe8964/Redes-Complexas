import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


all_data_sets = [
    "abide",
    "neurocon",
    "ppmi",
    "taowu",
]

all_measures = [
    "assortativity",
    "average_degree",
    "betweeness_centrality",
    "closeness_centrality",
    "eigen_centrality",
    "k_core",
    "ratio",
]

data_sets = [
    "abide",
    "neurocon",
    "ppmi",
    "taowu",
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

shelf = shelve.open("./shelfs/the_thresholds")
the_thresholds = shelf["data"]
shelf.close()

shelf = shelve.open("./shelfs/the_useless_thresholds")
the_useless_thresholds = shelf["data"]
shelf.close()

for from_data_set in data_sets:
    for measure in measures:
        useful = "useless"
        for thresholds in [the_thresholds, the_useless_thresholds]:
            if useful == "useless":
                useful = "useful"
            else:
                useful = "useless"
            for subjects_min in ["nmin"]:
                shelf = shelve.open("./shelfs/df_" + measure + "_" + subjects_min + "_" + from_data_set)
                df = shelf["data"]
                shelf.close()

                threshold = thresholds[from_data_set][measure]
               
                for type in ["control", "patient"]:
                    df[type] = df[type][df[type].threshold == threshold]
                    del df[type]["threshold"]

                value_counts = {"control": df["control"].value_counts().sort_index(),
                                "patient": df["patient"].value_counts().sort_index()}

                to_plot = {"control": {"x": value_counts["control"].index.get_level_values(0).values,
                                       "y": value_counts["control"].values.astype("float64")},
                           "patient": {"x": value_counts["patient"].index.get_level_values(0).values,
                                       "y": value_counts["patient"].values.astype("float64")}}

                #n = 30
                #for type in ["control", "patient"]:
                #    for i in range(to_plot[type]["y"].size):
                #        to_plot[type]["y"][i] /= n

                title = f"{from_data_set} - {measure} - {subjects_min} - {useful} threshold of value {threshold}"

                plt.plot(to_plot["control"]["x"], to_plot["control"]["y"], label="control")
                plt.plot(to_plot["patient"]["x"], to_plot["patient"]["y"], label="patient")
                plt.legend()
                plt.title(title)
                plt.xlabel(measure)
                plt.ylabel("count")
                plt.savefig(f"./useful/{title}.png")
                #plt.show()
        
                del df
