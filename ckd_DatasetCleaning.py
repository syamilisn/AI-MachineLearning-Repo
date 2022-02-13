import pandas as pd
import numpy as np

dataset = pd.read_csv('chronic_kidney_disease.csv')
#print(dataset)
data = list()
for i in dataset:
    print(i)