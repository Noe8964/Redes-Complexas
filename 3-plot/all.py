import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()

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
    "eigen_centrality",
]

for from_data_set in ["abide", "ppmi"]:
    for measure in all_measures:
        shelf = shelve.open("./shelfs/" + measure + "_" + from_data_set)
        measure_data = shelf["data"]
        shelf.close()
        
        for subjects_min in ["min", "nmin"]:
            match subjects_min:
                case "min":
                    n = min(len(measure_data["control"]), len(measure_data["patient"]))

                    df_creator = {"control": {"threshold": thresholds.tolist()*n, "data": []},
                                  "patient": {"threshold": thresholds.tolist()*n, "data": []}}

                    for type in ["control", "patient"]:
                        for i in range(n):
                            df_creator[type]["data"] += measure_data[type][i]
                case "nmin":
                    df_creator = {"control": {"threshold": thresholds.tolist()*len(measure_data["control"]), "data": []},
                                  "patient": {"threshold": thresholds.tolist()*len(measure_data["patient"]), "data": []}}

                    for type in ["control", "patient"]:
                        for i in range(len(measure_data[type])):
                            df_creator[type]["data"] += measure_data[type][i]

            """ print(len(measure_data["control"][0]))
            print(len(measure_data["patient"][0]))
            print()

            print(len(df_creator["control"]["threshold"]))
            print(len(df_creator["control"]["data"]))
            print(len(df_creator["patient"]["threshold"]))
            print(len(df_creator["patient"]["data"]))
            print()

            quit() """

            df = {"control": pd.DataFrame(df_creator["control"]),
                  "patient": pd.DataFrame(df_creator["patient"])}
            
            sns.set_theme(style="darkgrid")
            sns.lineplot(data=df["control"], x="threshold", y="data", label="control")
            sns.lineplot(data=df["patient"], x="threshold", y="data", label="patient")
            plt.title(from_data_set + " " + measure)
            plt.xlabel("threshold")
            plt.ylabel(measure)
            plt.legend()
            plt.savefig("./images/" + measure + "/" + measure + "_" + from_data_set + "_" + subjects_min + ".png")
            plt.close()
            #plt.show()

            shelf = shelve.open("./shelfs/df" + "_" + measure + "_" + subjects_min + "_" + from_data_set)
            shelf["data"] = df
            shelf.close()

            del df_creator
            del df
        
        del measure_data
