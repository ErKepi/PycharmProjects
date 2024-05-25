import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 10 * (np.sin(x))**2

x = np.linspace(0, 2 * np.pi, 1000)

y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = 10 \cdot (\sin(x))^2$', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph von f(x)=10·(sin(x))2')
plt.legend()
plt.grid(False)

plt.show()