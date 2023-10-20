import shelve
import math
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"].tolist()
shelf.close()

accuracy = {
    "abide": {
        "assortativity": 0,
        "average_degree": 0,
        "betweeness_centrality": 0,
        "closeness_centrality": 0,
        "eigen_centrality": 0,
        "k_core": 0,
        "ratio": 0,
    },
    "neurocon": {
        "assortativity": 0,
        "average_degree": 0,
        "betweeness_centrality": 0,
        "closeness_centrality": 0,
        "eigen_centrality": 0,
        "k_core": 0,
        "ratio": 0,
    },
    
    "ppmi": {
        "assortativity": 0,
        "average_degree":  0,
        "betweeness_centrality": 0,
        "closeness_centrality": 0,
        "eigen_centrality": 0,
        "k_core": 0,
        "ratio": 0,
    },
    "taowu": {
        "assortativity": 0,
        "average_degree": 0,
        "betweeness_centrality": 0,
        "closeness_centrality": 0,
        "eigen_centrality": 0,
        "k_core": 0,
        "ratio": 0,
    },
}

all_measures = [
    "assortativity",
    "average_degree",
    "betweeness_centrality",
    "closeness_centrality",
    "eigen_centrality",
    "k_core",
    "ratio",
]

all_data_sets = [
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

data_sets = [
    "abide",
    "neurocon",
    "ppmi",
    "taowu",
]

shelf = shelve.open("./shelfs/the_thresholds")
the_thresholds = shelf["data"]
shelf.close()

for from_data_set in data_sets:
    for measure in measures:
        shelf = shelve.open("./shelfs/" + measure + "_" + from_data_set)
        measure_data = shelf["data"]
        shelf.close()

        the_threshold = the_thresholds[from_data_set][measure]

        wanted_measure_data = {"control": [], "patient": []}

        for type in ["control", "patient"]:
            for subject in measure_data[type]:
                wanted_measure_data[type].append(subject[thresholds.index(the_threshold)])
        
        del measure_data
        
        # handle nan
        if measure == "assortativity":
            for type in ["control", "patient"]:
                for i in range(len(wanted_measure_data[type])):
                    if math.isnan(wanted_measure_data[type][i]):
                        wanted_measure_data[type][i] = -1

        X = wanted_measure_data["control"] + wanted_measure_data["patient"]     
        y = [0]*len(wanted_measure_data["control"]) + [1]*len(wanted_measure_data["patient"])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        X_train = np.array(X_train).reshape(-1, 1)
        X_test = np.array(X_test).reshape(-1, 1)

        neigh = KNeighborsClassifier(n_neighbors=3)
        neigh.fit(X_train, y_train)

        y_pred = neigh.predict(X_test)

        accuracy[from_data_set][measure] = round(accuracy_score(y_test, y_pred), 2)

shelf = shelve.open("./shelfs/accuracy")
shelf["data"] = accuracy
shelf.close()

for from_data_set in data_sets:
    print(from_data_set)
    for measure in measures:
        print(accuracy[from_data_set][measure])
