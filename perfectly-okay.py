import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the Gaussian distribution
mu = 0  # Mean
sigma = 1  # Standard deviation

# Generate data points
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mu, sigma)

# Identify "abnormal" normal events (center of the distribution)
abnormal_region = (x > -1) & (x < 1)
normal_region = ~abnormal_region

# Plot the Gaussian distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Gaussian Distribution")

# Highlight abnormal events
plt.fill_between(x, y, where=abnormal_region, color="red", alpha=0.5, label="Abnormal Normal Events")
plt.fill_between(x, y, where=normal_region, color="blue", alpha=0.3, label="Normal Events")

# Highlight outliers (tails)
outlier_region = (x < -3) | (x > 3)
plt.fill_between(x, y, where=outlier_region, color="orange", alpha=0.7, label="Abnormal Outliers")

# Labels and legend
plt.title("Gaussian Event Graph: Redefining Normal and Abnormal Events")
plt.xlabel("Event Value")
plt.ylabel("Probability Density")
plt.legend(loc="upper left")
plt.grid(True)

# Show the plot
plt.show()