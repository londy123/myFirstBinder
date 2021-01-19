import numpy as np
data = np.loadtxt('SH300PREU.csv',delimiter = ',', skiprows=1)

x , y , z  = data[:,1] , data[:,2] , data[:,3]

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()

from scipy.optimize import curve_fit

def func(data, a, b, c):
    return data[:,0]*a + data[:,1]*b + c

guess = (1,1,1)

params, pcov = curve_fit(func, data[:,1:3], data[:,3],guess)
print(params)