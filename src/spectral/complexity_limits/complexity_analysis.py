import matplotlib.pyplot as plt
import numpy as np

# Valeurs de n à tester
n = np.array([50, 75, 100, 125, 150, 175, 200])

# Taille totale du système : N = (n+1)^2
N = (n + 1) ** 2

# Coût mémoire ~ O(N)
cout_memoire = N

# Coût en temps pour k valeurs propres ~ O(k·N)
k = 60
cout_temps = k * N

# Tracer les deux courbes sur des sous-graphes séparés
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Graphique 1 : mémoire
ax1.plot(n, cout_memoire, label='Mémoire ~ O(n²)', marker='o', \
         color='blue')
ax1.set_ylabel("Mémoire (taille de la matrice)")
ax1.set_title("Croissance de la mémoire avec n")
ax1.grid(True)
ax1.legend()

# Graphique 2 : temps
ax2.plot(n, cout_temps, label='Temps pour k modes ~ O(k·n²)', marker='s', \
         color='orange')
ax2.set_xlabel("n (taille du maillage)")
ax2.set_ylabel("Temps de calcul")
ax2.set_title("Croissance du temps de calcul avec n")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()