import numpy as np
import matplotlib.pyplot as plt

p = 100  # nombre d’intervalles
x = np.linspace(-1, 1, p + 1)
y = np.linspace(-1, 1, p + 1)
h = 2 / p
m = 3
n = 2
dt = h / 2
T = 10  # temps total de simulation

# Initialisation des conditions initiales
X, Y = np.meshgrid(x, y, indexing='ij')
Uo = np.cos(m * np.pi * X) * np.cos(n * np.pi * Y) + \
     np.cos(n * np.pi * X) * np.cos(m * np.pi * Y)
Uoo = Uo.copy()

U = np.zeros_like(Uo)
nb_past = int(T / dt)

for t in range(nb_past):
    for i in range(p + 1):
        for j in range(p + 1):

            i_1 = i - 1 if i > 0 else 1
            i1 = i + 1 if i < p else p - 1
            j_1 = j - 1 if j > 0 else 1
            j1 = j + 1 if j < p else p - 1

            U[i, j] = ((Uo[i_1, j] - 4 * Uo[i, j] + Uo[i1, j] +
                        Uo[i, j_1] + Uo[i, j1])
                       / h**2 * dt**2 - Uoo[i, j] + 2 * Uo[i, j])

    Uoo = Uo.copy()
    Uo = U.copy()

# Affichage de la surface 3D finale
fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(121, projection='3d')
X_plot, Y_plot = np.meshgrid(x, y)
ax1.plot_surface(X_plot, Y_plot, U, cmap='viridis')
ax1.set_title("Surface finale U(x,y)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("U")

# Affichage des lignes nodales (contour niveau 0)
ax2 = fig.add_subplot(122)
ax2.contour(x, y, U.T, levels=[0], colors='red')
ax2.set_title("Contours niveau 0 (lignes nodales)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()