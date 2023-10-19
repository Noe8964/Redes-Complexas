import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from_data_set = "ppmi"

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"].tolist()
shelf.close()

shelf = shelve.open("./shelfs/ratio_" + from_data_set)
ratio = shelf["data"]
shelf.close()

the_threshold = 0.4

wanted_measure = {"control": [], "patient": []}

for type in ["control", "patient"]:
    for subject in ratio[type]:
        wanted_measure[type].append(subject[thresholds.index(the_threshold)])

del ratio

X = wanted_measure["control"] + wanted_measure["patient"]
y = [0]*len(wanted_measure["control"]) + [1]*len(wanted_measure["patient"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

X_train = np.array(X_train).reshape(-1, 1)
X_test = np.array(X_test).reshape(-1, 1)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

y_pred = neigh.predict(X_test)

print(accuracy_score(y_test, y_pred))
