import shelve
import networkx as nx
centrality = {"control": [], "patient": []}

from_data_set = "abide"

if from_data_set == "abide":
    shelf = shelve.open("./shelfs/filtered_networks_abide_control")
    filtered_networks_abide_control = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_control["abide"]["control"]:
        subject_centrality = []
        for network in subject:
            subject_centrality.append(nx.degree_assortativity_coefficient(network))
        centrality["control"].append(subject_centrality)

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
elif from_data_set == "ppmi":
    shelf = shelve.open("./shelfs/filtered_networks_ppmi")
    filtered_networks = shelf["data"]
    shelf.close()
    
    for type in ["control", "patient"]:
        for subject in filtered_networks["ppmi"][type]:
            subject_centrality = []
            for network in subject:
                nodes_centrality=nx.betweenness_centrality(network)
                subject_centrality.append(sum(list(nodes_centrality.values()))/len(nodes_centrality))
            centrality[type].append(subject_centrality) 
        print(centrality[type])
        print(len(centrality[type]))
shelf = shelve.open("./shelfs/Centrality_in_beetween_" + from_data_set)
shelf["data"] = centrality
shelf.close()
