import shelve
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"]
shelf.close()

measures = "assortativities", "average_degrees", "betweeness_centrality", "closeness_centrality", "eigen_centrality", "max_k_core_sizes", "ratios"

for from_data_set in ["ppmi"]:
    for measure in ["closeness_centrality", "eigen_centrality"]:
        shelf = shelve.open("./shelfs/" + measure + "_" + from_data_set)
        measure_data = shelf["data"]
        shelf.close()
        
        for subjects_min in ["min", "nmin"]:
            match subjects_min:
                case "min":
                    n = min(len(measure_data["control"]), len(measure_data["patient"]))

                    data_frame_creator = {"control": {"threshold": thresholds.tolist()*n, "data": []},
                                          "patient": {"threshold": thresholds.tolist()*n, "data": []}}

                    for type in ["control", "patient"]:
                        for i in range(n):
                            data_frame_creator[type]["data"] += measure_data[type][i]
                case "nmin":
                    data_frame_creator = {"control": {"threshold": thresholds.tolist()*len(measure_data["control"]), "data": []},
                                          "patient": {"threshold": thresholds.tolist()*len(measure_data["patient"]), "data": []}}

                    for type in ["control", "patient"]:
                        for i in range(len(measure_data[type])):
                            data_frame_creator[type]["data"] += measure_data[type][i]

            print(from_data_set)
            print(measure)
            print(subjects_min)
            print()
            print(len(data_frame_creator["control"]["data"]))
            print(len(data_frame_creator["patient"]["data"]))

            quit()

            df = {"control": pd.DataFrame(data_frame_creator["control"]),
                  "patient": pd.DataFrame(data_frame_creator["patient"])}
            
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
        
        del measure_data
