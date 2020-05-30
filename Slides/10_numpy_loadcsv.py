import numpy as np
file = np.loadtxt("num.csv",delimiter= ',')
print(file)

file = np.loadtxt("num.csv",delimiter= ',', skiprows=1)
print(file)

file = np.loadtxt("num.csv",delimiter= ',', usecols=[2,4])
print(file)

file = np.loadtxt("num.csv",delimiter= ',', usecols=[2,4], dtype=str)
print(file)