import shelve
import networkx as nx

for centrality_type in ["betweeness", "closeness"]:
    match centrality_type:
        case "betweeness":
            f = nx.betweenness_centrality
        case "closeness":
            f = nx.closeness_centrality

    for from_data_set in ["abide", "ppmi"]:
        centrality = {"control": [], "patient": []}

        if from_data_set == "abide":
            for type in ["control", "patient"]:
                shelf = shelve.open("./shelfs/filtered_networks_abide_" + type)
                filtered_networks_abide_type = shelf["data"]
                shelf.close()

                for subject in filtered_networks_abide_type["abide"][type]:
                    subject_centrality = []
                    for network in subject:
                        nodes_centrality = f(network)
                        subject_centrality.append(sum(list(nodes_centrality.values()))/len(nodes_centrality))
                    centrality[type].append(subject_centrality)

                del filtered_networks_abide_type
        elif from_data_set == "ppmi":
            shelf = shelve.open("./shelfs/filtered_networks_ppmi")
            filtered_networks = shelf["data"]
            shelf.close()

            for type in ["control", "patient"]:
                for subject in filtered_networks["ppmi"][type]:
                    subject_centrality = []
                    for network in subject:
                        nodes_centrality = f(network)
                        subject_centrality.append(sum(list(nodes_centrality.values()))/len(nodes_centrality))
                    centrality[type].append(subject_centrality)

        shelf = shelve.open("./shelfs/" + centrality_type + "_centrality_" + from_data_set)
        shelf["data"] = centrality
        shelf.close()

        del centrality
