import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

def build_custom_B(n):
    B = np.zeros((n+1, n+1))
    for i in range(n+1):
        B[i, i] = -4
        if i > 0:
            B[i, i-1] = 1
        if i < n:
            B[i, i+1] = 1
    B[0, 0] = 2
    B[n, n] = 2
    return sp.csr_matrix(B)

def build_custom_D(n, h=1.0):
    B = build_custom_B(n)
    I_block = sp.eye(n+1, format='csr')
    J = 2 * I_block

    blocks = []
    for row in range(n+1):
        row_blocks = []
        for col in range(n+1):
            if row == col:
                row_blocks.append(B)
            elif abs(row - col) == 1:
                if row == 0 or row == n:
                    row_blocks.append(J)
                else:
                    row_blocks.append(I_block)
            else:
                row_blocks.append(sp.csr_matrix((n+1, n+1)))
        blocks.append(row_blocks)

    D = sp.bmat(blocks, format='csr') / (h**2)
    return D

# Constantes physiques
a = 0.18  # m
c = 54.5  # m/s

# Construction de D pour n = 100
n = 100
D = build_custom_D(n)

# Fréquences cibles uniformément espacées
f_target = np.linspace(0, 1000, 10)
omega_target = 2 * np.pi * f_target
lambda_target = - (a / c)**2 * omega_target**2

# Recherche des valeurs propres proches
true_lambdas = []
true_frequencies = []

for target in lambda_target:
    eigval, _ = spla.eigsh(D, k=1, sigma=target, which='LM')
    true_lambdas.append(eigval[0])
    true_frequencies.append((a / c) * np.sqrt(-eigval[0]))

# Résultat
for f, lam, lfound, wphys in zip(f_target, lambda_target, true_lambdas, true_frequencies):
    print(f"f_target = {f:.1f} Hz | lambda_target = {lam:.3f} | "
          f"lambda_trouvee = {lfound:.6f} | w_phys = {wphys:.2f} Hz")