import shelve

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
    average_degree = {"control": [], "patient": []}
    
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
            average_degree["control"].append(subject_average_degrees)
    
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
            average_degree["patient"].append(subject_average_degrees)
    
        del filtered_networks_abide_patient
    else:
        shelf = shelve.open("./shelfs/filtered_networks_" + from_data_set)
        filtered_networks = shelf["data"]
        shelf.close()
    
        for type in ["control", "patient"]:
            for subject in filtered_networks[from_data_set][type]:
                subject_average_degrees = []
                for network in subject:
                    average = 0
                    for k in network.degree:
                        average += k[1]
                    average /= len(network.nodes())
                    subject_average_degrees.append(average)
                average_degree[type].append(subject_average_degrees)

        del filtered_networks
        
    shelf = shelve.open("./shelfs/average_degree_" + from_data_set)
    shelf["data"] = average_degree
    shelf.close()

    del average_degree
