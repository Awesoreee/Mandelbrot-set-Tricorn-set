import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(z, pow, conj, iterMax):
  c = -0.8 + 1j * 0
  for n in range(iterMax):
    if abs(z) > 2:
      return n
    if conj:
      z = np.conj(np.power(z, pow)) + c
    else:
      z = np.power(z, pow) + c
  return iterMax

def mandelbrotShow(xmin, xmax, ymin, ymax, width, height, pow = 2, conj = 0, iterMax = 256):
  x = np.linspace(xmin, xmax,width)
  y = np.linspace(ymin, ymax, height)
  mandelbrotGrid = np.zeros((height, width))
 
  for i in range(height):
    for j in range(width):
      mandelbrotGrid[i,j] = mandelbrot(x[j] + 1j * y[i], pow, conj, iterMax)
 
  return mandelbrotGrid

#Границы
xmin = -2
xmax = 2
ymin = -2
ymax = 2

#Разрешение
width, height = 1600, 1600

#Степень
power = 2

#Кол-во итераций
iterMax = 50

#Сопряжённое (1) 
conj = 0

mandelbrotGrip = mandelbrotShow(xmin, xmax, ymin, ymax, width, height, power, conj, iterMax)

plt.figure(figsize=(10,10))
plt.imshow(mandelbrotGrip, extent=(xmin, xmax, ymin, ymax), cmap='turbo_r', origin='lower')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()