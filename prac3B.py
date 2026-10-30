import matplotlib.pyplot as plt  # For plotting graphs
import numpy as np  # For generating random numbers
import scipy.stats as st  # For the normal distribution function

np.random.seed(0)  # Fix the random seed so results are reproducible
# mu = mean, sigma = standard deviation, numBins = number of histogram bars
mu, sigma, numBins = 90, 25, 35

# Generate 5000 random values from a normal distribution (mean 90, std dev 25)
x = mu + sigma * np.random.randn(5000)
# Plot the histogram; density=True scales bars so the total area is 1
n, bins, patches = plt.hist(x, numBins, color="Orange", density=True, alpha=1)
# Calculate the theoretical normal curve at each bin edge
y = st.norm.pdf(bins, mu, sigma)
# Overlay the curve as a dashed line to compare with the histogram
plt.plot(bins, y, "--")
# Build a title showing the sample size, bins and parameters (mu/sigma in LaTeX style)
plt.title(
    "Histogram "
    + str(len(x))
    + " entries into "
    + str(numBins)
    + " bins: $\\mu="
    + str(mu)
    + "$, $\\sigma="
    + str(sigma)
    + "$"
)
plt.xlabel("Example Data")
plt.ylabel("Probability Density")
plt.show()  # Display the plot
