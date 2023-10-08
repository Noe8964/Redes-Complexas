import shelve
import scipy.io
import networkx as nx
import pandas as pd
import numpy as np

control = pd.DataFrame(scipy.io.loadmat("./data/abide/control/sub-control50030/sub-control50030_AAL116_correlation_matrix.mat")["data"])
patient = pd.DataFrame(scipy.io.loadmat("./data/abide/control/sub-control50030/sub-control50030_AAL116_correlation_matrix.mat")["data"])

control = control.apply(lambda x : np.where(x == 1, 0, x))
patient = patient.apply(lambda x : np.where(x == 1, 0, x))

data = {"control": [], "patient": []}

thresholds = np.linspace(-1, 1, 21)

for threshold in thresholds: 
    data["control"].append(nx.from_pandas_adjacency(control.apply(lambda x : np.where(x < threshold, 0, x))))
    data["patient"].append(nx.from_pandas_adjacency(patient.apply(lambda x : np.where(x < threshold, 0, x))))

shelf = shelve.open("./shelfs/filtered_networks")
shelf["data"] = data
shelf.close()

shelf = shelve.open("./shelfs/ratios")
shelf["thresholds"] = thresholds
shelf.close()
