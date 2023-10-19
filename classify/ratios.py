import shelve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wot = "ppmi"
_min = "min"

shelf = shelve.open("./shelfs/probability_" + wot + "_ratios")
data = shelf["data"]
shelf.close()

print(data)


