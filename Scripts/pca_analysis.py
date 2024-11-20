import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Placeholder for peptide conformations (100 samples, 20 features)
data = np.random.rand(100, 20)

# PCA to reduce dimensions to 2
pca = PCA(n_components=2)
pca_results = pca.fit_transform(data)

# Plotting PCA results
plt.scatter(pca_results[:, 0], pca_results[:, 1], alpha=0.7)
plt.title("Principal Component Analysis (PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid()
plt.savefig("pca_results.png")
print("PCA plot saved as 'pca_results.png'.")
