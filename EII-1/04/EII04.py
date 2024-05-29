import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 10 * (np.sin(x))**2

# linspace(start, stop, Punkte die dazwischen liegen)
x = np.linspace(-5, 5, 100)

# Berechnen von x
y = f(x)

plt.plot(x, y)

# Labels fuer den Graphen, x- und y-Achse
plt.title('$f(x) = 10 \cdot (\sin(x))^2$')
plt.xlabel('x')
plt.ylabel('y')

# Grid einblenden = True; Grid ausblenden = False
plt.grid(False)
# print(x)

# Ausgabe Wertetabelle
print(f(x))

# Ausgabe Graph
plt.show()

