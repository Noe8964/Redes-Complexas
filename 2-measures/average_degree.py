import shelve
import networkx as nx
import matplotlib.pyplot as plt

average_degrees = {"control": [], "patient": []}

from_data_set = "ppmi"

if from_data_set == "abide":
    shelf = shelve.open("./shelfs/filtered_networks_abide_control")
    filtered_networks_abide_control = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_control["abide"]["control"]:
        subject_average_degrees = []
        for network in subject:
            average = 0
            for k in network.degree:
                average += k[1]
            average /= len(network.nodes())
            subject_average_degrees.append(average)
        average_degrees["control"].append(subject_average_degrees)

    del filtered_networks_abide_control

    shelf = shelve.open("./shelfs/filtered_networks_abide_patient")
    filtered_networks_abide_patient = shelf["data"]
    shelf.close()

    for subject in filtered_networks_abide_patient["abide"]["patient"]:
        subject_average_degrees = []
        for network in subject:
            average = 0
            for k in network.degree:
                average += k[1]
            average /= len(network.nodes())
            subject_average_degrees.append(average)
        average_degrees["patient"].append(subject_average_degrees)

    del filtered_networks_abide_patient
elif from_data_set == "ppmi":
    shelf = shelve.open("./shelfs/filtered_networks_ppmi")
    filtered_networks = shelf["data"]
    shelf.close()

    for type in ["control", "patient"]:
        for subject in filtered_networks["ppmi"][type]:
            subject_average_degrees = []
            for network in subject:
                average = 0
                for k in network.degree:
                    average += k[1]
                average /= len(network.nodes())
                subject_average_degrees.append(average)
            average_degrees[type].append(subject_average_degrees)

shelf = shelve.open("./shelfs/average_degrees_" + from_data_set)
shelf["data"] = average_degrees
shelf.close()
