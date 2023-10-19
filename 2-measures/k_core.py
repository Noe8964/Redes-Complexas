import shelve
import networkx as nx

max_k_core_sizes = {"control": [], "patient": []}

from_data_set = "ppmi"

if from_data_set == "abide":
    shelf = shelve.open("./shelfs/filtered_networks_abide_control")
    filtered_networks_abide_control = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_control["abide"]["control"]:
        subject_max_k_core_sizes = []
        for network in subject:
            network_giant_component = network.subgraph(sorted(nx.connected_components(network), key=len, reverse=True)[0])
            subject_max_k_core_sizes.append(len(network_giant_component.nodes())/len(network.nodes()))
        max_k_core_sizes["control"].append(subject_max_k_core_sizes)

    del filtered_networks_abide_control

    shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
    filtered_networks_abide_patient = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_patient["abide"]["patient"]:
        subject_max_k_core_sizes = []
        for network in subject:
            network_giant_component = network.subgraph(sorted(nx.connected_components(network), key=len, reverse=True)[0])
            subject_max_k_core_sizes.append(len(network_giant_component.nodes())/len(network.nodes()))
        max_k_core_sizes["patient"].append(subject_max_k_core_sizes)

    del filtered_networks_abide_patient
elif from_data_set == "ppmi":
    shelf = shelve.open("./shelfs/filtered_networks_ppmi")
    filtered_networks = shelf["data"]
    shelf.close()

    for type in ["control", "patient"]:
        for subject in filtered_networks["ppmi"][type]:
            subject_max_k_core_sizes = []
            for network in subject:
                subject_max_k_core_sizes.append(len(nx.k_core(G=network, k=max(nx.core_number(network))).nodes()))
            max_k_core_sizes[type].append(subject_max_k_core_sizes)
            

shelf = shelve.open("./shelfs/max_k_core_sizes_" + from_data_set)
shelf["data"] = max_k_core_sizes
shelf.close()
