import shelve

the_thresholds = {
    "abide": {
        "assortativity": 0.8,
        "average_degree": 0,
        "betweeness_centrality": 0.5,
        "closeness_centrality": 0,
        "eigen_centrality": 0.8,
        "k_core": 0.5,
        "ratio": 0.5,
    },
    "ppmi": {
        "assortativity": 0.8,
        "average_degree": -0.3,
        "betweeness_centrality": 0.5,
        "closeness_centrality": 0.5,
        "eigen_centrality": 0.9,
        "k_core": -0.7,
        "ratio": 0.8,
    },
}

shelf = shelve.open("./shelfs/the_thresholds")
shelf["data"] = the_thresholds
shelf.close()
