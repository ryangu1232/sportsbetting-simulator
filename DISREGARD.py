import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

odds = [1,2,3,4]
result_array = []

repititions = 100

def runsim():
    global result_array
    choice = np.random.choice(odds)
    if choice == 4:
        result_array = np.append(result_array, "hit")
    else: 
        result_array = np.append(result_array, "miss")
    return result_array

for i in np.arange(1000):
    result_array = np.append(result_array, runsim())




