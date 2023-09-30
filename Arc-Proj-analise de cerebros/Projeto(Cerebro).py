import networkx as nx
import numpy as np
from scipy import io
import pandas as pd
import matplotlib.pyplot as plt
matrix = io.loadmat('sub-control50030_AAL116_correlation_matrix.mat')
# Create an empty graph
G = nx.Graph()
data= pd.DataFrame(matrix['data'])
data_filtered=data.apply(lambda x:np.where(x==1,0,x))
data_filtered=data_filtered.apply(lambda x:np.where(x<0.5,0,x))
G = nx.from_pandas_adjacency(data_filtered)
print(len(G.nodes()))
pos = nx.spring_layout(G, iterations=15, seed=1721)
fig, ax = plt.subplots(figsize=(15, 9))
ax.axis("off")
nx.draw_networkx(G, pos=pos, ax=ax,)

