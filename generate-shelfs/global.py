import shelve
import numpy as np

shelf = shelve.open("./shelfs/global")

shelf["thresholds"] = np.linspace(-1, 1, 21)

shelf["the_threshold"] = 0.25

shelf.close()