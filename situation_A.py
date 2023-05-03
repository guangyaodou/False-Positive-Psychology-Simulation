import numpy as np
from scipy.stats import ttest_ind

np.random.seed(0)

# set up simulation parameters
num_simulations = 15000  # number of simulations to run
sample_size = 20  # sample size for each group
mean_1 = 0  # true mean for group 1
std_dev = 1  # standard deviation for both groups
corr = 0.5  # correlation between dependent variables

# generate dependent variables with specified correlation
cov_matrix = np.array([[1, corr], [corr, 1]])
# dependent_vars = np.random.multivariate_normal([0, 0], cov_matrix, size=sample_size)

# initialize lists to store results
p_values = []

# run simulations
for i in range(num_simulations):
    # generate random data for both groups
    group_1 = np.random.multivariate_normal([mean_1, mean_1], cov_matrix, size=sample_size)
    null_hypothesis = np.random.normal(loc=mean_1, scale=std_dev, size=sample_size)
    # this null hypothesis has the same mean and standard deviation as the dependent variables we
    # obtained from multivariate normal distribution
    dep_var1 = group_1[:, 0]
    dep_var2 = group_1[:, 1]
    dep_mean = (dep_var1 + dep_var2) / 2

    # calculate t-test p-value for each situation
    p_value_1 = ttest_ind(dep_var1, null_hypothesis)[1]
    if p_value_1 < 0.05:
        p_values.append(p_value_1)
    else:
        p_value_2 = ttest_ind(dep_var2, null_hypothesis)[1]
        if p_value_2 < 0.05:
            p_values.append(p_value_2)
        else:
            p_value_3 = ttest_ind(dep_mean, null_hypothesis)[1]
            if p_value_3 < 0.05:
                p_values.append(p_value_3)

# print the results
print(len(p_values))
print("Percentage of significant results", round(len(p_values) / num_simulations, 3))
