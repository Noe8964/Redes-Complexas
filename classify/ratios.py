import shelve
import pandas as pd

wot = "ppmi"

shelf = shelve.open("./shelfs/data_frame_ratios_" + wot)
df = shelf["data"]
shelf.close()

the_threshold = 0.7

for type in ["control", "patient"]:
    df[type] = df[type][df[type].threshold == the_threshold]
    print(df[type])

