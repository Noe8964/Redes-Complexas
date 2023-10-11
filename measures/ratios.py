import shelve
import networkx as nx

shelf = shelve.open("./shelfs/filtered_networks")
ratios_mean = shelf["data"]
shelf.close()

ratios = {"control": [], "patient": []}

for type in ["control", "patient"]:
    for network in filtered_networks[type]:
        network_giant_component = network.subgraph(sorted(nx.connected_components(network), key=len, reverse=True)[0])
        ratios[type].append(len(network_giant_component.nodes())/len(network.nodes()))

shelf = shelve.open("./shelfs/ratios")
shelf["data"] = ratios
shelf.close()

