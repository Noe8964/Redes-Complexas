import shelve
import networkx as nx

for from_data_set in ["abide", "ppmi"]:
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
    elif from_data_set == "ppmi":
        shelf = shelve.open("./shelfs/filtered_networks_ppmi")
        filtered_networks = shelf["data"]
        shelf.close()

        for type in ["control", "patient"]:
            for subject in filtered_networks["ppmi"][type]:
                subject_assortativies = []
                for network in subject:
                    subject_assortativies.append(nx.degree_assortativity_coefficient(network))
                assortativity[type].append(subject_assortativies)

    shelf = shelve.open("./shelfs/assortativity_" + from_data_set)
    shelf["data"] = assortativity
    shelf.close()

    del assortativity
