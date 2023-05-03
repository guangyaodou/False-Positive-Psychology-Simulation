import numpy as np
from scipy.stats import ttest_ind


np.random.seed(0)
# set up simulation parameters
num_simulations = 15000  # number of simulations to run
sample_size = 20  # sample size for each group
mean_1 = 0  # true mean for group 
std_dev = 1  # standard deviation for both groups
alpha = 0.05


p_values = []

# run simulations
for i in range(num_simulations):
    # generate random data from a Normal Distribution
    group = np.random.normal(loc=mean_1, scale=std_dev, size=20)
    
    Group_1=group

    null_hypothesis = np.random.normal(loc=mean_1, scale=std_dev, size=20)
    # Group_2=group[10:20]
    
    p_value=ttest_ind(Group_1, null_hypothesis)[1]

    if p_value < alpha:
        p_values.append(p_value)
    else:
        add_group=np.random.normal(loc=mean_1, scale=std_dev, size=10)
        Group_1 = np.append(add_group,Group_1)

        p_value2=ttest_ind(Group_1, null_hypothesis)[1]
        p_values.append(p_value2)
        

# count the number of times each dependent variable had a significant p-value

count=0
for i in range(15000):
    if p_values[i]<alpha:
        count=count+1

# print the results
print(round(count / num_simulations, 3))
