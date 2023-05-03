import numpy as np
from scipy.stats import ttest_ind

np.random.seed(0)
samples_size = 15000
observations_per_cell = 20
corr = 0.5
cov_matrix = np.array([[1, corr], [corr, 1]])
alpha = 0.05

simulated_observations = np.random.multivariate_normal((0, 0), cov_matrix, size=samples_size)

cells_observation_1 = []
cells_observation_2 = []
cells_mean = []
for i in range(simulated_observations.shape[0] // observations_per_cell):
    sample_1 = simulated_observations[i * 20:i * 20 + 20, 0]
    sample_2 = simulated_observations[i * 20:i * 20 + 20, 1]
    sample_mean = (sample_1 + sample_2 / 2)
    cells_observation_1.append(sample_1)
    cells_observation_2.append(sample_2)
    cells_mean.append(sample_mean)

null_hypothesis = np.random.normal(size=20)
reject = 0
additional_observations = np.random.multivariate_normal((0, 0), cov_matrix, size=10)
additional_1 = additional_observations[:, 0]
additional_2 = additional_observations[:, 1]
additional_mean = (additional_1 + additional_2) / 2

for i in range(len(cells_observation_1)):
    if ttest_ind(cells_observation_1[i], null_hypothesis)[1] < alpha:
        reject += 1
    elif ttest_ind(cells_observation_2[i], null_hypothesis)[1] < alpha:
        reject += 1
    elif ttest_ind(cells_mean[i], null_hypothesis)[1] < alpha:
        reject += 1
    elif ttest_ind(np.concatenate((cells_observation_1[i], additional_1))[10:], cells_observation_1[i][10:])[1] < alpha:
        reject += 1
    elif ttest_ind(np.concatenate((cells_observation_2[i], additional_2))[10:], cells_observation_2[i][10:])[1] < alpha:
        reject += 1
    elif ttest_ind(np.concatenate((cells_mean[i], additional_mean))[10:], cells_mean[i][:10])[1] < alpha:
        reject += 1

print("The percentage of Rejection is:", reject / len(cells_observation_1))
