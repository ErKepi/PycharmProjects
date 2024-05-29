import numpy as np
import matplotlib.pyplot as plt

# Erzeugen der x-Werte
x = np.linspace(-10, 10, 100)

# Berechnen der y-Werte für die Funktion f(x) = x^2
y = x ** 2

# Erstellen der Wertetabelle
wertetabelle = np.column_stack((x, y))
print("Wertetabelle (x, f(x)):")
print(wertetabelle)

# Visualisieren der Werte
plt.plot(x, y, label='f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph der Funktion f(x) = x^2')
plt.legend()
plt.grid(True)
plt.show()
