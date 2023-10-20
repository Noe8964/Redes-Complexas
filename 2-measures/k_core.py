import shelve
import networkx as nx

all_data_sets = [
    "abide",
    "neurocon",
    "ppmi",
    "taowu",
]

data_sets = [
    "neurocon",
    "taowu",
]

for from_data_set in data_sets:
    max_k_core_sizes = {"control": [], "patient": []}

    if from_data_set == "abide":
        #! THIS WAS WRONG, RUN THIS AGAIN
        
        shelf = shelve.open("./shelfs/filtered_networks_abide_control")
        filtered_networks_abide_control = shelf["data"]
        shelf.close()

        for subject in filtered_networks_abide_control["abide"]["control"]:
            subject_max_k_core_sizes = []
            for network in subject:
                subject_max_k_core_sizes.append(len(nx.k_core(G=network, k=max(nx.core_number(network))).nodes()))
            max_k_core_sizes["control"].append(subject_max_k_core_sizes)

        del filtered_networks_abide_control

        shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
        filtered_networks_abide_patient = shelf["data"]
        shelf.close()

        for subject in filtered_networks_abide_patient["abide"]["patient"]:
            subject_max_k_core_sizes = []
            for network in subject:
                    subject_max_k_core_sizes.append(len(nx.k_core(G=network, k=max(nx.core_number(network))).nodes()))
            max_k_core_sizes["patient"].append(subject_max_k_core_sizes)

        del filtered_networks_abide_patient
    else:
        shelf = shelve.open("./shelfs/filtered_networks_" + from_data_set) 
        filtered_networks = shelf["data"]
        shelf.close()

        for type in ["control", "patient"]:
            for subject in filtered_networks[from_data_set][type]:
                subject_max_k_core_sizes = []
                for network in subject:
                    subject_max_k_core_sizes.append(len(nx.k_core(G=network, k=max(nx.core_number(network))).nodes()))
                max_k_core_sizes[type].append(subject_max_k_core_sizes)
        
        del filtered_networks

    shelf = shelve.open("./shelfs/k_core_" + from_data_set)
    shelf["data"] = max_k_core_sizes
    shelf.close()

    del max_k_core_sizes
