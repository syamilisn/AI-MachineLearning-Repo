import matplotlib.pyplot as plt
from numpy import full
import pandas as pd

col_list = ["Location_3L","Pressure_3L","Location_6L","Pressure_6L","Location_12L","Pressure_12L"]
full_data= pd.read_excel("pressure_data_grid.xlsx",usecols=col_list)

LocX_3L=(full_data[col_list[0]].dropna())
Pressure_3L=(full_data[col_list[1]].dropna())
LocX_6L=(full_data[col_list[2]].dropna())
Pressure_6L=(full_data[col_list[3]].dropna())
LocX_12L=(full_data[col_list[4]].dropna())
Pressure_12L=(full_data[col_list[5]].dropna())



fig, ax = plt.subplots()
ax.tick_params(axis='both', which='major', labelsize=15)
plt.plot(LocX_3L,Pressure_3L)
plt.plot(LocX_6L,Pressure_6L)
plt.plot(LocX_12L,Pressure_12L)
plt.legend(["Pressure 3L","Pressure 6L","Pressure_12L"])
plt.show()