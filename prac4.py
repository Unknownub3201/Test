import numpy as np 
from pandas.io.formats.style import _background_gradient
from scipy import stats 
import matplotlib.pyplot as plt 

np.random.seed(42)

sample1 = np.random.normal(loc=10, scale=2, size=30)
sample2 = np.random.normal(loc=12, scale=2, size=30)

t_stat, p_value = stats.ttest_ind(sample1, sample2)

alpha = 0.05
print("Results of Two-Sample t-test: ")
print(f"t-statistics: {t_stat}")
print(f"p-value: {p_value}")
print(f"Degree of Freedom: {len(sample1) + len(sample2) - 2}")

# Plot 
plt.figure(figsize=(10,6))
plt.hist(sample1, alpha=0.5, label='Sample 1', color='blue')
plt.hist(sample2, alpha=0.5, label='Sample 2', color='orange')
plt.axvline(np.mean(sample1), color='blue', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(sample2), color='orange', linestyle='dashed', linewidth=2)
plt.title('Distributions of Sample 1 and Sample 2')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()

# High the critical region if null hypothesis is rejected 
if p_value < alpha:
    critical_region = np.linspace(min(sample1.min(), sample2.min()), max(sample1.max(), sample2.max()), 1000)
    plt.fill_between(critical_region, 0, 5, color='red', alpha=0.3, label='Critical Region')

# Show observed t-statistics
plt.text(11, 5, f't-statistics:{t_stat:.2f}', ha='center', va='center', color='black', backgroundcolor='white')

plt.show()

if p_value < alpha:
    if np.mean(sample1) > np.mean(sample2):
        print("Conclusion: There is significant evidence to reject the null hypothesis")
        print("Interpretation: The mean caffeine content of Sample 1 is significantly higher than that of Sample 2.")
    elif np.mean(sample1) < np.mean(sample2):
        print("Conclusion: There is significant evidence to reject the null hypothesis")
        print("Interpretation: The mean caffeine content of Sample 2 is significantly higher than that of Sample 1.")
    else: 
        print("Conclusion: Failed to reject the null hypothesis.")
        print("Interpretation: There is not enough evidence to claim a significant difference between the means.")