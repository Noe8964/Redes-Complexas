import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from_data_set = "ppmi"
_min = "min"

shelf = shelve.open("./shelfs/probability_" + from_data_set + "_ratios")
data = shelf["data"]
shelf.close()

print(data)


