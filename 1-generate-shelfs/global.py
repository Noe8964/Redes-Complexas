import shelve
import numpy as np

thresholds = np.linspace(-1, 1, 21)

for i in range(thresholds.size):
    thresholds[i] = round(thresholds[i], 1)

shelf = shelve.open("./shelfs/global")
shelf["thresholds"] = thresholds
shelf.close()
