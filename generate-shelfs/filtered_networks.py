import shelve
import scipy.io
import networkx as nx
import pandas as pd
import numpy as np

data = {"control": [], "patient": []}

control = pd.DataFrame(scipy.io.loadmat("./data/abide/control/sub-control50030/sub-control50030_AAL116_correlation_matrix.mat")["data"])
patient = pd.DataFrame(scipy.io.loadmat("./data/abide/patient/sub-patient50002/sub-patient50002_AAL116_correlation_matrix.mat")["data"])

control = control.apply(lambda x : np.where(x == 1, 0, x))
patient = patient.apply(lambda x : np.where(x == 1, 0, x))

shelf = shelve.open("./shelfs/ratios")
thresholds = shelf["thresholds"]
shelf.close()

for threshold in thresholds: 
    data["control"].append(nx.from_pandas_adjacency(control.apply(lambda x : np.where(x < threshold, 0, x))))
    data["patient"].append(nx.from_pandas_adjacency(patient.apply(lambda x : np.where(x < threshold, 0, x))))

shelf = shelve.open("./shelfs/filtered_networks")
shelf["data"] = data
shelf.close()
