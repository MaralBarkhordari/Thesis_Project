import numpy as np
import matplotlib.pyplot as plt

# Placeholder for dihedral angle data (phi, psi pairs)
phi_psi_angles = np.random.rand(100, 2) * 360 - 180  # Random angles between -180° and 180°

# Plotting the dihedral angles
plt.scatter(phi_psi_angles[:, 0], phi_psi_angles[:, 1], alpha=0.7)
plt.title("Dihedral Angle Distribution (φ, ψ)")
plt.xlabel("φ (phi)")
plt.ylabel("ψ (psi)")
plt.grid()
plt.savefig("dihedral_angles.png")
print("Dihedral angle plot saved as 'dihedral_angles.png'.")
