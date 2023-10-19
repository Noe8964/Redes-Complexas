import shelve
import networkx as nx
centrality = {"control": [], "patient": []}

wot = "abide"
if wot == "abide":
    shelf = shelve.open("./shelfs/filtered_networks_abide_control")
    filtered_networks_abide_control = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_control["abide"]["control"]:
        subject_centrality = []
        for network in subject:
            nodes_centrality=nx.eigenvector_centrality(network,max_iter=10000)
            subject_centrality.append(sum(list(nodes_centrality.values()))/len(nodes_centrality))
        centrality["control"].append(subject_centrality)

    del filtered_networks_abide_control

    shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
    filtered_networks_abide_patient = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_patient["abide"]["patient"]:
        ssubject_centrality = []
        for network in subject:
            nodes_centrality=nx.eigenvector_centrality(network,max_iter=10000)
            subject_centrality.append(sum(list(nodes_centrality.values()))/len(nodes_centrality))
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
                nodes_centrality=nx.eigenvector_centrality(network,max_iter=10000)
                subject_centrality.append(sum(list(nodes_centrality.values()))/len(nodes_centrality))
            centrality[type].append(subject_centrality) 
        print(centrality[type])
        print(len(centrality[type]))

shelf = shelve.open("./shelfs/Eigen_centrality_" + wot)
shelf["data"] = centrality
shelf.close()