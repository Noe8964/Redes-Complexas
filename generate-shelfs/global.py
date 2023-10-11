import shelve
import numpy as np

shelf = shelve.open("./shelfs/global")

shelf["thresholds"] = np.linspace(-1, 1, 21)

shelf.close()