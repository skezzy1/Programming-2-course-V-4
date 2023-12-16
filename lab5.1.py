import matplotlib.pyplot as plt
import math
import numpy as np

def f(x,y,a):
    result = (math.log(a+(x/y)**3)-math.sin(y-a)**4)/(math.sqrt(math.sin(x+y/x-y)**3))
    return result
cube = lambda x : x**3

a = float(input("a: "))
b = float(input("b: "))
n = int(input("Enter number of breakpoints:"))
x = np.linspace(a, b, n)
y = (4 * x) / (x**2 - 4)
plt.plot(x, y, label='f(x) = 4x/ (x^2 - 4)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Графік функції f(x)')
plt.show()