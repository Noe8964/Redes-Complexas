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
    assortativity = {"control": [], "patient": []}
    
    if from_data_set == "abide":
        shelf = shelve.open("./shelfs/filtered_networks_abide_control")
        filtered_networks_abide_control = shelf["data"]
        shelf.close()

        for subject in filtered_networks_abide_control["abide"]["control"]:
            subject_assortativies = []
            for network in subject:
                subject_assortativies.append(nx.degree_assortativity_coefficient(network))
            assortativity["control"].append(subject_assortativies)

        del filtered_networks_abide_control

        shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
        filtered_networks_abide_patient = shelf["data"]
        shelf.close()

        for subject in filtered_networks_abide_patient["abide"]["patient"]:
            subject_assortativies = []
            for network in subject:
                subject_assortativies.append(nx.degree_assortativity_coefficient(network))
            assortativity["patient"].append(subject_assortativies)

        del filtered_networks_abide_patient
    else:
        shelf = shelve.open("./shelfs/filtered_networks_" + from_data_set)
        filtered_networks = shelf["data"]
        shelf.close()

        for type in ["control", "patient"]:
            for subject in filtered_networks[from_data_set][type]:
                subject_assortativies = []
                for network in subject:
                    subject_assortativies.append(nx.degree_assortativity_coefficient(network))
                assortativity[type].append(subject_assortativies)
        
        del filtered_networks

    shelf = shelve.open("./shelfs/assortativity_" + from_data_set)
    shelf["data"] = assortativity
    shelf.close()

    del assortativity
