import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset1 = pd.read_excel(io="D:/OneDrive/Lightweight Design Lab Data/Testing_machine "
                             "data/0_degrees_01_20230523_1255976.xlsx", header=4,usecols = [0,3,7])
dataset1 = dataset1.drop(0)

dataset2 = pd.read_excel(io="D:/OneDrive/Lightweight Design Lab Data/Testing_machine data/mix_02_20230523_1255661.xlsx",
                         header=4,usecols = [0,3,7])
dataset2 = dataset2.drop(0)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(7, 5), dpi=200)

sns.lineplot(x='Traverse',y='Kraft',data=dataset1,label='0° Sample', color='red')
sns.lineplot(x='Traverse',y='Kraft',data=dataset2,label='[0/90/45/-45]s Sample', color='blue')

plt.xlabel(r"Displacement (mm) $\longrightarrow$")
plt.ylabel(r"Load (N) $\longrightarrow$")
plt.title("Load-Displacement Curves")
plt.show()

dataset1['Strain'] = dataset1['Traverse']/251
dataset2['Strain'] = dataset2['Traverse']/251

area1 = ((1.12+1.18+1.14)/3)*((24.76+24.78+24.72)/3)
area2 = ((24.52+24.72+24.46)/3)*((2.02+2.04+2.20)/3)

dataset1['Stress'] = dataset1['Kraft']/area1
dataset2['Stress'] = dataset2['Kraft']/area2

sns.set_theme(style="whitegrid")
plt.figure(figsize=(7, 5), dpi=200)

sns.lineplot(x='Strain',y='Stress',data=dataset1,label='0° Sample', color='red')
sns.lineplot(x='Strain',y='Stress',data=dataset2,label='[0/90/45/-45]s Sample', color='blue')
plt.xlabel(r"Strain $\longrightarrow$")
plt.ylabel(r"Stress (MPa) $\longrightarrow$")
plt.title("Stress-Strain Curves")
plt.show()


dataset3 = pd.read_excel(io="D:/OneDrive/Lightweight Design Lab Data/EXT Data/0deg_sp1.xlsx", header=0)
dataset4 = pd.read_excel(io="D:/OneDrive/Lightweight Design Lab Data/EXT Data/Mix_Sp2.xlsx", header=0)

print(dataset3.head(20))
print("========================================")
print(dataset4.head(20))

sns.set_theme(style="whitegrid")
plt.figure(figsize=(7,5), dpi=200)

sns.lineplot(x='Strain',y='Stress',data=dataset3, color='red', label='0° Sample')
sns.lineplot(x='Strain',y='Stress',data=dataset4, color='blue', label ='[0/90/45/-45]s Sample')
plt.xlabel(r"Strain (mm/mm) $\longrightarrow$")
plt.ylabel(r"Stress (MPa) $\longrightarrow$")
plt.xlim(0,0.015)
plt.title("Stress-Strain Curves")
plt.show()
