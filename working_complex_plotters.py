# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:04:30 2021

@author: therm
"""

"""
This file contains the plotting tools that worked
"""

#%%
"""
This is a tool to visualise the magnitude, and the real and imaginary components of a complex function's 
output. 

comp_func() accepts the real and imaginary axis, computes values for a complex function f(z), and returns an
array
The complex function being used can be changed within comp_func()
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 13.5
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"

def comp_func(X, Y):
    z = X + Y*1j
    return np.log(z)

#define an xy grid
n = 300 #grid resolution
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)


f_z = comp_func(X, Y)

real_f = f_z.real
imag_f = f_z.imag
magnit = abs(f_z)

plt.plot(X, real_f, '.', color = 'black')
plt.xlabel("Real Axis")
plt.ylabel("$Re[f(z)]$")
plt.show()

plt.plot(X, magnit, '.', color = 'blue')
plt.xlabel("Real Axis")
plt.ylabel("Magnitude of $f(z)$")
plt.show()

plt.plot(X, imag_f, '.', color = 'orange')
plt.xlabel("Real Axis")
plt.ylabel("$Im[f(z)]$")
plt.show()

#%%
"""
Plotting the magnitude of f(z) but using a contour plot
"""
import numpy as np
import matplotlib.pyplot as plt

def comp_func(X, Y):
    z = X + Y*1j
    return np.log(z)

#define an xy grid
n = 300 #grid resolution
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)

Z = comp_func(X, Y)

plt.contour(X, Y, abs(Z), 20, cmap='inferno')
plt.axis('equal')
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("Contour Plot for $|f(z)|$")
plt.colorbar();

#%%
"""
How about 3D plotting?: https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

ALso kinda works. Mainly worth it for plotting the 
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def comp_func3D(X, Y):
    Z = X + Y*1j
    return np.log(Z)

#define an xy grid
n = 300 #grid resolution
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)

Z = comp_func3D(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(X, Y, abs(Z), marker = '.', cmap = "Greens")
ax.set_xlabel('Real Axis')
ax.set_ylabel('Imaginary Axis')
ax.set_zlabel('$|f(z)|$')
plt.show()






