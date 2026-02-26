import numpy as np
import matplotlib.pyplot as plt

# Données expérimentales : fréquences et vitesses estimées
frequences = np.array([149, 154, 440, 751.769, 1047, 3768])  # en Hz
c_estimé = np.array([53.64, 19.601, 56.003, 63.79, 75.384, 170.496])  # en m/s

# Régression linéaire avec numpy.polyfit
coeffs = np.polyfit(frequences, c_estimé, deg=1)  # Ajustement linéaire
fit_line = np.polyval(coeffs, frequences)  # Valeurs ajustées pour la droite

# Tracé du graphique
plt.figure(figsize=(8, 6))
plt.scatter(frequences, c_estimé, label='Valeurs estimées de c', marker='o')
plt.plot(frequences, fit_line, linestyle='--',
         label=f"Régression : c = {coeffs[0]:.2f}f + {coeffs[1]:.2f}")

plt.xlabel("Fréquence (Hz)")
plt.ylabel("Vitesse estimée c (m/s)")
plt.title("Echec du modèle de d'Alembert à haute fréquence")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()