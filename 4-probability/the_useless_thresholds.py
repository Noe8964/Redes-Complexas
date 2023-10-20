import shelve

the_useless_thresholds = {
    "abide": {
        "assortativity": 0.7,
        "average_degree": 0,
        "betweeness_centrality": 0.4,
        "closeness_centrality": 0,
        "eigen_centrality": 0.4,
        "k_core": 0.5,
        "ratio": 0.5,
    },
    "neurocon": {
        "assortativity": 0.7,
        "average_degree": 0,
        "betweeness_centrality": 0.3,
        "closeness_centrality": 0,
        "eigen_centrality": 0.2,
        "k_core": -0.2,
        "ratio": 0.3,
    },
    "ppmi": {
        "assortativity": 0.4,
        "average_degree": 0,
        "betweeness_centrality": 0,
        "closeness_centrality": 0,
        "eigen_centrality": 0.1,
        "k_core": -0.4,
        "ratio": 0.8,
    },
    "taowu": {
        "assortativity": 0.7,
        "average_degree": 0,
        "betweeness_centrality": 0.6,
        "closeness_centrality": 0,
        "eigen_centrality": 0.1,
        "k_core": -0.6,
        "ratio": 0.6,
    },
}

shelf = shelve.open("./shelfs/the_useless_thresholds")
shelf["data"] = the_useless_thresholds
shelf.close()
