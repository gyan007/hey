import numpy as np
import matplotlib.pyplot as plt

def plot_gaussian(mean=0.0, std_dev=1.0, size=1000, bins=30):
    # Generate random samples from a normal distribution
    data = np.random.normal(loc=mean, scale=std_dev, size=size)

    # Plot normalized histogram (density=True makes it a probability density)
    plt.hist(data, bins=bins, density=True, alpha=0.6, edgecolor='black', label='Samples')

    # Create x values for the theoretical PDF
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)

    # Overlay the theoretical Gaussian curve
    plt.plot(x, pdf, linewidth=2, label=f'Normal PDF (μ={mean}, σ={std_dev})')

    plt.title("Gaussian (Normal) Distribution")
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Accept user input (with defaults if user presses Enter)
    try:
        mean_input = input("Enter mean (default 0.0): ").strip()
        mean = float(mean_input) if mean_input else 0.0

        std_input = input("Enter standard deviation (default 1.0): ").strip()
        std_dev = float(std_input) if std_input else 1.0
        if std_dev <= 0:
            raise ValueError("Standard deviation must be positive.")

        size_input = input("Enter sample size (default 1000): ").strip()
        size = int(size_input) if size_input else 1000
        if size <= 0:
            raise ValueError("Sample size must be positive integer.")

        bins_input = input("Enter number of bins for histogram (default 30): ").strip()
        bins = int(bins_input) if bins_input else 30
        if bins <= 0:
            raise ValueError("Bins must be positive integer.")
    except ValueError as e:
        print("Invalid input:", e)
    else:
        plot_gaussian(mean=mean, std_dev=std_dev, size=size, bins=bins)
