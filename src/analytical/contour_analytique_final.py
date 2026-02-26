import numpy as np
import matplotlib.pyplot as plt

# Grille spatiale
n = 200
x = np.linspace(0, 1, n+1)
y = np.linspace(0, 1, n+1)
X, Y = np.meshgrid(x, y)
m1, n1 = 2, 3
m2, n2 = 3, 2

# Modes propres
U_1 = np.cos(m1 * np.pi * X) * np.cos(m2 * np.pi * Y)
U_2 = np.cos(m2 * np.pi * X) * np.cos(n2 * np.pi * Y)

# Tracé des lignes nodales
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Mode (2,3)
axs[0].contour(X, Y, U_1, levels=[0], colors='blue')
axs[0].set_title(r"Lignes nodales pour $\cos(2\pi x) \cos(3\pi y)$")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].set_aspect('equal')

# Mode (3,2)
axs[1].contour(X, Y, U_2, levels=[0], colors='red')
axs[1].set_title(r"Lignes nodales pour $\cos(3\pi x) \cos(2\pi y)$")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].set_aspect('equal')

plt.tight_layout()
plt.show()

# Superposition

# Modes propres
m1, n1 = 2, 3
m2, n2 = 3, 2

# Combinaison linéaire avec A = B = 1
U = np.cos(m1 * np.pi * X) * np.cos(n1 * np.pi * Y) + \
    np.cos(m2 * np.pi * X) * np.cos(n2 * np.pi * Y)

# --- Tracé 3D ---
fig1 = plt.figure(figsize=(10,6))
ax = fig1.add_subplot(121, projection='3d')
surf = ax.plot_surface(X, Y, U, cmap='viridis')
ax.set_title(r"Surface 3D: $u(x,y)$ pour $\omega = \pi \sqrt{13}$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Amplitude")
fig1.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# --- Tracé des lignes nodales ---
ax2 = fig1.add_subplot(122)
contours = ax2.contour(X, Y, U, levels=[0], colors='purple')
ax2.set_title("Lignes nodales (u=0)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()