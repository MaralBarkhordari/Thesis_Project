import numpy as np

# Placeholder: Two conformations of a peptide (3D coordinates)
conformation1 = np.random.rand(15, 3)  # 15 atoms
conformation2 = np.random.rand(15, 3)

# Calculate RMSD
def calculate_rmsd(conf1, conf2):
    diff = conf1 - conf2
    rmsd = np.sqrt(np.mean(np.sum(diff**2, axis=1)))
    return rmsd

rmsd_value = calculate_rmsd(conformation1, conformation2)
print(f"RMSD between two conformations: {rmsd_value:.2f} Å")
