import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

np.random.seed(0)
samples_size = 15000
observations_per_cell = 20
alpha = 0.05

condition = np.random.choice(3, samples_size)
dataset = pd.DataFrame(condition, columns=["conditions"])
dataset["data"] = np.random.normal(size=samples_size)

reject = 0
for i in range(samples_size):
    low = np.random.choice(dataset[dataset.conditions == 0]["data"].to_numpy(), observations_per_cell)
    medium = np.random.choice(dataset[dataset.conditions == 1]["data"].to_numpy(), observations_per_cell)
    high = np.random.choice(dataset[dataset.conditions == 2]["data"].to_numpy(), observations_per_cell)
    if ttest_ind(low, medium)[1] < alpha:
        reject += 1
    elif ttest_ind(high, medium)[1] < alpha:
        reject += 1
    elif ttest_ind(high, low)[1] < alpha:
        reject += 1

print("The percentage of rejection is ", reject / samples_size)
