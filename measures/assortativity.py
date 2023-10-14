import shelve
import networkx as nx

assortativities = {"control": [], "patient": []}

wot = "ppmi"

if wot == "abide":
    shelf = shelve.open("./shelfs/filtered_networks_abide_control")
    filtered_networks_abide_control = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_control["abide"]["control"]:
        subject_assortativies = []
        for network in subject:
            subject_assortativies.append(nx.degree_assortativity_coefficient(network))
        assortativities["control"].append(subject_assortativies)

    del filtered_networks_abide_control

    shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
    filtered_networks_abide_patient = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_patient["abide"]["patient"]:
        subject_assortativies = []
        for network in subject:
            subject_assortativies.append(nx.degree_assortativity_coefficient(network))
        assortativities["patient"].append(subject_assortativies)

    del filtered_networks_abide_patient
elif wot == "ppmi":
    shelf = shelve.open("./shelfs/filtered_networks_ppmi")
    filtered_networks = shelf["data"]
    shelf.close()

    for type in ["control", "patient"]:
        for subject in filtered_networks["ppmi"][type]:
            subject_assortativies = []
            for network in subject:
                subject_assortativies.append(nx.degree_assortativity_coefficient(network))
            assortativities[type].append(subject_assortativies)

shelf = shelve.open("./shelfs/assortativities_" + wot)
shelf["data"] = assortativities
shelf.close()
