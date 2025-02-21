import numpy as np
import matplotlib.pyplot as plt

def main():
    # Membuat data untuk classification secara manual
    np.random.seed(42)
    X_class = np.random.rand(100, 2) * 10
    sum_features = X_class[:, 0] + X_class[:, 1]
    y_class = (sum_features > 10).astype(int)
    
    # Membuat data untuk regression secara manual
    X_reg = np.random.rand(100, 1) * 10
    y_reg = 2 * X_reg[:, 0] + np.random.randn(100) * 2
    
    # Membuat figure dan axes
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Scatter plot untuk classification
    scatter = axs[0].scatter(X_class[:, 0], X_class[:, 1], c=y_class, cmap='viridis', edgecolor='k', s=100)
    axs[0].set_title("Classification Data", fontsize=14, fontweight='bold', color='darkblue')
    axs[0].set_xlabel("Feature 1", fontsize=12, fontstyle='italic')
    axs[0].set_ylabel("Feature 2", fontsize=12, fontstyle='italic')
    legend1 = axs[0].legend(*scatter.legend_elements(), title="Classes", loc='upper right', fontsize='small')
    axs[0].add_artist(legend1)
    axs[0].grid(True, linestyle='--', linewidth=0.5)
    
    # Plot 2: Scatter plot untuk regression
    axs[1].scatter(X_reg, y_reg, color='blue', edgecolor='k', s=100)
    axs[1].set_title("Regression Data", fontsize=14, fontweight='bold', color='darkgreen')
    axs[1].set_xlabel("Feature", fontsize=12, fontstyle='italic')
    axs[1].set_ylabel("Target", fontsize=12, fontstyle='italic')
    axs[1].grid(True, linestyle='--', linewidth=0.5)
    
    # Menambahkan layout yang rapi
    fig.tight_layout()
    
    # Menyimpan plot ke file
    fig.savefig("machine_learning_visualization_with_numpy.png")
    
    # Menampilkan plot
    plt.show()

if __name__ == "__main__":
    main()