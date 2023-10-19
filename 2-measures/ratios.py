import shelve
import networkx as nx

ratios = {"control": [], "patient": []}

for from_data_set in ["abide", "ppmi"]:
    if from_data_set == "abide":
        shelf = shelve.open("./shelfs/filtered_networks_abide_control")
        filtered_networks_abide_control = shelf["data"]
        shelf.close()

        for subject in filtered_networks_abide_control["abide"]["control"]:
            subject_ratios = []
            for network in subject:
                network_giant_component = network.subgraph(sorted(nx.connected_components(network), key=len, reverse=True)[0])
                subject_ratios.append(len(network_giant_component.nodes())/len(network.nodes()))
            ratios["control"].append(subject_ratios)

        del filtered_networks_abide_control

        shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
        filtered_networks_abide_patient = shelf["data"]
        shelf.close()

        for subject in filtered_networks_abide_patient["abide"]["patient"]:
            subject_ratios = []
            for network in subject:
                network_giant_component = network.subgraph(sorted(nx.connected_components(network), key=len, reverse=True)[0])
                subject_ratios.append(len(network_giant_component.nodes())/len(network.nodes()))
            ratios["patient"].append(subject_ratios)

        del filtered_networks_abide_patient
    elif from_data_set == "ppmi":
        shelf = shelve.open("./shelfs/filtered_networks_ppmi")
        filtered_networks = shelf["data"]
        shelf.close()

        for type in ["control", "patient"]:
            for subject in filtered_networks["ppmi"][type]:
                subject_ratios = []
                for network in subject:
                    network_giant_component = network.subgraph(sorted(nx.connected_components(network), key=len, reverse=True)[0])
                    subject_ratios.append(len(network_giant_component.nodes())/len(network.nodes()))
                ratios[type].append(subject_ratios)

    shelf = shelve.open("./shelfs/ratios_" + from_data_set)
    shelf["data"] = ratios
    shelf.close()
