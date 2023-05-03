import numpy as np
import pandas as pd
from pingouin import ancova
from scipy.stats import ttest_ind

np.random.seed(1)
num_simulation = 15000
observations_per_cell = 20
additional_size = 10
corr_dv = 0.5
corr = 0
cov_matrix = np.array(
    [[1, corr_dv], [corr_dv, 1]])
alpha = 0.05

mean = 0

rejection = 0

for i in range(num_simulation):

    null_hypothesis = np.random.normal(size=20)
    print(f"Combined_ABC is running {i}th simulation")
    # Simulate data

    group = np.random.multivariate_normal(
        [mean, mean], cov_matrix, size=observations_per_cell)
    covar = np.random.normal(size=observations_per_cell)
    gender = np.random.binomial(1, 0.5, size=observations_per_cell)  # gender (0 = male, 1 = female)
    data = pd.DataFrame({'dependent_var1': group[:, 0],
                         'dependent_var2': group[:, 1],
                         'average_var3': (group[:, 0] + group[:, 1]) / 2,
                         'covar': covar,
                         'gender': gender})
    additional_group = np.random.multivariate_normal(
        [mean, mean], cov_matrix, size=additional_size)
    covar_additional = np.random.normal(size=additional_size)
    additional_gender = np.random.binomial(1, 0.5, size=additional_size)
    additional = pd.DataFrame({'dependent_var1': additional_group[:, 0],
                               'dependent_var2': additional_group[:, 1],
                               'average_var3': (additional_group[:, 0] + additional_group[:, 1]) / 2,
                               'covar': covar_additional,
                               'gender': additional_gender})
    additional_data = pd.concat([data, additional], ignore_index=True)
    group_men = data[data.gender == 0]
    group_women = data[data.gender == 1]
    additional_group_men = additional_data[additional_data.gender == 0]
    additional_group_women = additional_data[additional_data.gender == 1]

    data["interaction"] = data["covar"] * data["gender"]
    additional_data["interaction"] = additional_data["covar"] * additional_data["gender"]

    if ttest_ind(data["dependent_var1"].to_numpy(), null_hypothesis)[1] < alpha:
        rejection += 1
    elif ttest_ind(data["dependent_var2"].to_numpy(), null_hypothesis)[1] < alpha:
        rejection += 1
    elif ttest_ind(((data["dependent_var1"] + data["dependent_var2"]) / 2).to_numpy(),
                   null_hypothesis)[1] < alpha:
        rejection += 1
    elif ttest_ind(additional_data["dependent_var1"].to_numpy(), null_hypothesis)[1] < alpha:
        rejection += 1
    elif ttest_ind(additional_data["dependent_var2"].to_numpy()[:10], null_hypothesis)[1] < alpha:
        rejection += 1
    elif ttest_ind(((additional_data["dependent_var1"] + additional_data["dependent_var2"]) / 2).to_numpy(),
                   null_hypothesis)[1] < alpha:
        rejection += 1
    elif ancova(data=data, dv='dependent_var1', covar='covar', between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=data, dv='dependent_var2', covar='covar', between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=additional_data, dv='dependent_var1', covar='covar', between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=additional_data, dv='dependent_var2', covar='covar', between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=data, dv='dependent_var1', covar=['covar', "interaction"], between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=data, dv='dependent_var2', covar=['covar', "interaction"], between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=additional_data, dv='dependent_var1', covar=['covar', "interaction"], between='gender')["p-unc"][
        0] < alpha:
        rejection += 1
    elif ancova(data=additional_data, dv='dependent_var2', covar=['covar', "interaction"], between='gender')["p-unc"][
        0] < alpha:
        rejection += 1
    elif ancova(data=data, dv='average_var3', covar=['covar', "interaction"], between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=additional_data, dv='average_var3', covar=['covar', "interaction"], between='gender')["p-unc"][
        0] < alpha:
        rejection += 1
    elif ancova(data=data, dv='average_var3', covar='covar', between='gender')["p-unc"][0] < alpha:
        rejection += 1
    elif ancova(data=additional_data, dv='average_var3', covar='covar', between='gender')["p-unc"][0] < alpha:
        rejection += 1

prop_significant_t = rejection / num_simulation
print(f"Proportion of significant effects for t tests: {prop_significant_t:.4f}")
