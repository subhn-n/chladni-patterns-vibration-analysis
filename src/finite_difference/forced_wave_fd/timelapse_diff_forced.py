import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(-1, 1, n + 1)
y = np.linspace(-1, 1, n + 1)
alpha = 5
h = 2 / n
dt = h / 2
T = 20

# Fréquence résonnante correcte
w = np.pi * np.sqrt(3**2 + 2**2)

def force(alpha, w, t):
    return alpha * np.cos(w * t)

U0 = np.zeros((n + 1, n + 1))
Uoo = np.zeros((n + 1, n + 1))
U = np.zeros((n + 1, n + 1))

nb_pas = int(T / dt)

# 5x5 = 25 images
nb_capture = 25
intervalle_temps = nb_pas // nb_capture

images = []
temps = []

t = 0
while t < nb_pas:
    for i in range(n + 1):
        for j in range(n + 1):
            if not (i == (n + 1) // 2 and j == (n + 1) // 2):

                i_1 = i - 1 if i > 0 else 1
                i1 = i + 1 if i < n else n - 1
                j_1 = j - 1 if j > 0 else 1
                j1 = j + 1 if j < n else n - 1

                U[i, j] = (
                    ((U0[i_1, j] - 4 * U0[i, j] + U0[i1, j]
                      + U0[i, j_1] + U0[i, j1]) / h**2) * dt**2
                    - Uoo[i, j] + 2 * U0[i, j]
                )

    pc = (n + 1) // 2
    U[pc, pc] = (
        ((U0[pc - 1, pc] - 4 * U0[pc, pc] + U0[pc + 1, pc]
          + U0[pc, pc - 1] + U0[pc, pc + 1]) / h**2
         + force(alpha, w, t * dt)) * dt**2
        - Uoo[pc, pc] + 2 * U0[pc, pc]
    )

    Uoo = U0.copy()
    U0 = U.copy()

    if t % intervalle_temps == 0:
        images.append(U.copy())
        temps.append(t * dt)

    t += 1

# =========================
# Affichage final 5x5
# =========================

fig, axs = plt.subplots(5, 5, figsize=(12, 10))

for k, ax in enumerate(axs.flat):
    cs = ax.contour(images[k], levels=[0])
    ax.set_title(f"t = {temps[k]:.1f}")
    ax.axis('off')

plt.tight_layout()
plt.show()