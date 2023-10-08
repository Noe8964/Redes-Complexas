import scipy.io
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


control = pd.DataFrame(scipy.io.loadmat("./data/abide/control/sub-control50030/sub-control50030_AAL116_correlation_matrix.mat")["data"])
control = control.apply(lambda x : np.where(x == 1, 0, x))

patient = pd.DataFrame(scipy.io.loadmat("./data/abide/control/sub-control50030/sub-control50030_AAL116_correlation_matrix.mat")["data"])
patient = patient.apply(lambda x : np.where(x == 1, 0, x))

control_ratios = []
patient_ratios = []

thresholds = np.linspace(-1, 1, 21)

print(thresholds)

for threshold in thresholds: 
    aux = control.apply(lambda x : np.where(x < threshold, 0, x))
    aux = nx.from_pandas_adjacency(aux)
    aux_gc = aux.subgraph(sorted(nx.connected_components(aux), key=len, reverse=True)[0])
    control_ratios.append(len(aux_gc.nodes())/len(aux.nodes()))

plt.plot(thresholds, control_ratios)
plt.show()