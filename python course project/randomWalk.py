import matplotlib.pyplot as plt
import numpy as np

def random_walk(n_points=1000):
    x = np.cumsum(np.random.randn(n_points))
    y = np.cumsum(np.random.randn(n_points))
    return x, y

if __name__ == "__main__":
    x, y = random_walk()
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, c=range(len(x)), cmap='viridis', s=10)
    plt.colorbar(label='Step')
    plt.title('Random Walk Simulation')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
