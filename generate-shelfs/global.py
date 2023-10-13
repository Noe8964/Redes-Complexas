import shelve
import numpy as np

shelf = shelve.open("./shelfs/global")

shelf["thresholds"] = np.linspace(-1, 1, 11)

shelf["the_threshold"] = 0.15

shelf.close()