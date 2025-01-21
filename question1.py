import numpy as np
from scipy.integrate import quad
# --- Question 1, Part 1: Monte Carlo Integration using Uniform(0,1) samples ---

# Define the function f(x) which is the integrand
def f(x):
    """
    Function representing the integrand: sin(x) / (x + cos^2(x))
    """
    return np.sin(x) / (x + np.cos(x)**2)

# Number of samples for Monte Carlo integration
monte_n_samples = 200  # Given in the question

# Generate monte_n_samples random numbers from Uniform(0,1)
monte_rand_samples = np.random.uniform(0, 1, monte_n_samples)

# Evaluate f(x) at the randomly sampled points
func_value = f(monte_rand_samples)

# Compute the Monte Carlo estimate of the integral
monte_integ_est_I_value = np.mean(func_value)  # Estimating the integral using the mean

# Print the result with reference to the question
print("Monte Carlo Estimate of I for Question 1, Part 1:", monte_integ_est_I_value) 


# --- Question 1, Part 2: Running Monte Carlo Integration 1000 times ---

# Define the function f(x), the same as in Part 1
def f(x):
    """
    Function representing the integrand: sin(x) / (x + cos^2(x))
    """
    return np.sin(x) / (x + np.cos(x)**2)

# Number of Monte Carlo repetitions
monte_repetitions = 1000  # Given in the question

# Number of samples per integration run
monte_n_samples = 200  # Same as in Part 1

# List to store all Monte Carlo estimates
monte_est_list = []

# Perform Monte Carlo integration 1000 times
for _ in range(monte_repetitions):
    # Generate monte_n_samples random numbers from Uniform(0,1)
    monte_rand_samples = np.random.uniform(0, 1, monte_n_samples)

    # Evaluate f(x) at the sampled points
    func_value = f(monte_rand_samples)

    # Compute the Monte Carlo estimate of the integral
    monte_integ_est_I_value = np.mean(func_value)

    # Store the estimate in the list
    monte_est_list.append(monte_integ_est_I_value)

# Convert to NumPy array for statistical calculations
monte_est_list = np.array(monte_est_list)

# Compute the mean and variance of the estimates
monte_mean_i_value = np.mean(monte_est_list)
monte_var_i_value = np.var(monte_est_list)

# Print results for Question 1, first part of Part 2 
print("Monte Carlo Results for Question 1, Part 2:")
print("Mean of 1000 Monte Carlo Estimates of I:", monte_mean_i_value)
print("Variance of 1000 Monte Carlo Estimates of I:", monte_var_i_value)

# To justify the accuracy of the numerical results. Second part of part 2
# Compute the true integral value using SciPy - scientific python
true_integral, error = quad(f, 0, 1)

# Print the result for Second part of part 2
print("True Integral Value (using quadrature):", true_integral)
print("Absolute Error of Monte Carlo Estimate:", abs(monte_mean_i_value - true_integral))

# Since the margin of error is only 0.00309, it is minimal. This indicates that the sample size of (n = 200) and the repetitions of 1000 were sufficient to justify the level of accuracy of our numerical results.
# In this case, this integral is one-dimensional. Hence, this method of comparing with traditional integration can be used to justify for accuracy. 
# Learning note: This is considered a close approximation to then true value. In situations where higher-dimensional integrals are involved in the calculation, where quadrature is not ideal method to used for measuring accurancy, we could utilize Confidence Intervals to measure Monte Carlo Accuracy.

