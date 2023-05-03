import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from scipy. stats import bernoulli

from pingouin import ancova


# set up simulation parameters
n = 20 # sample size
num_sims = 15000 # number of simulations to run

mean = 0.5  # true mean for group
std=1 #standard deviation for the group
 
p_values=[]

# run simulations
for i in range(num_sims):
    # generate random data from a Normal Distribution
    group = np.random.normal(mean,std, n)
    
    group1=group[0:10]
    group2=group[10:20]
    Group=np.concatenate((group1, group2))
    
    p_value1=ttest_ind(group1, group2)[1]

    if p_value1 < 0.05:
        p_values.append(p_value1)
    else:
        covariate = np.random.normal(size=n) # covariate
        gender = np.random.binomial(1, 0.5, size=n) # gender (0 = male, 1 = female)
        covar=covariate
        
        data = pd.DataFrame({'dependent_var1': Group,
                                 'covar': covar,
                                 'gender': gender})

        res1 = ancova(data=data, dv='dependent_var1', covar='covar', between='gender')
        p_val1 = res1["p-unc"][0]
        
        if p_val1 < 0.05:
            p_values.append(p_val1)
        else:

            data = pd.DataFrame({'dependent_var1': Group,
                                     'covar': covar,
                                     'gender': gender, 'interaction': covar*gender})
    
            res2 = ancova(data=data, dv='dependent_var1', covar=['interaction','covar'], between='gender')
            p_val2 = res2["p-unc"][0]
            p_values.append(p_val2)
               
print(len(p_values))

count=0
for i in range(len(p_values)):
    if p_values[i]<0.05:
        count=count+1

# print the results
print(round(count / num_sims, 3))
