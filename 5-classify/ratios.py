import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from_data_set = "ppmi"

shelf = shelve.open("./shelfs/global")
thresholds = shelf["thresholds"].tolist()
shelf.close()

shelf = shelve.open("./shelfs/ratios_" + from_data_set)
ratios = shelf["data"]
shelf.close()

the_threshold = 0.4

wanted_measure = {"control": [], "patient": []}

for type in ["control", "patient"]:
    print(len(ratios[type]))
    for subject in ratios[type]:
        wanted_measure[type].append(subject[thresholds.index(the_threshold)])

del ratios


X = wanted_measure["control"] + wanted_measure["patient"]
y = [0]*len(wanted_measure["control"]) + [1]*len(wanted_measure["patient"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
