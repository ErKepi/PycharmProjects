import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 10 * (np.sin(x)*np.sin(x))

x = np.linspace(0, 10, 1000)

y = f(x)

# plt.figure()
plt.plot(x, y)

# Labels fuer den Graphen, x- und y-Achse
plt.title('$f(x) = 10 \cdot (\sin(x))^2$')
plt.xlabel('x')
plt.ylabel('y')

# Grid einblenden = True; Grid ausblenden = False
plt.grid(False)

# Ausgabe
plt.show()