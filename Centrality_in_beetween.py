import shelve
import networkx as nx
centrality = {"control": [], "patient": []}

wot = "ppmi"
if wot == "abide":
    shelf = shelve.open("./shelfs/filtered_networks_abide_control")
    filtered_networks_abide_control = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_control["abide"]["control"]:
        subject_centrality = []
        for network in subject:
            subject_centrality.append(nx.degree_assortativity_coefficient(network))
        centrality["control"].append(subject_assortativies)

    del filtered_networks_abide_control

    shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
    filtered_networks_abide_patient = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_patient["abide"]["patient"]:
        ssubject_centrality = []
        for network in subject:
                nodes_centrality=nx.betweenness_centrality(network)
                print(sum(nodes_centrality)/len(nodes_centrality))
                subject_centrality.append(sum(nodes_centrality)/len(nodes_centrality))
        centrality["patient"].append(subject_centrality)

    del filtered_networks_abide_patient
elif wot == "ppmi":
    shelf = shelve.open("./shelfs/filtered_networks_ppmi")
    filtered_networks = shelf["data"]
    shelf.close()

    for type in ["control", "patient"]:
        for subject in filtered_networks["ppmi"][type]:
            subject_centrality = []
            for network in subject:
                nodes_centrality=nx.betweenness_centrality(network)
                print(sum(nodes_centrality)/len(nodes_centrality))
                subject_centrality.append(sum(nodes_centrality)/len(nodes_centrality))
                centrality[type].append(subject_centrality)

shelf = shelve.open("./shelfs/Centrality_in_beetween_" + wot)
shelf["data"] = centrality
shelf.close()
