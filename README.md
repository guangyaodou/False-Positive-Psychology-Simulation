# False-Positive-Psychology-Simulation

# Introduction
This is the replication of the simulation results in the paper [False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting 
Anything as Significant by Joseph P. Simmons, Leif D. Nelson, and Uri Simonsohn.](https://journals.sagepub.com/doi/pdf/10.1177/0956797611417632)
The authors present a detailed statistical analysis, using computer simulations, to test for the association between the number of researcher degrees of freedom and 
the likelihood of encountering false-positives, and propose a disclosure-based solution to address this problem by providing six requirements for authors and four 
guidelines for reviewers.

The authors conduct a simulation that assesses the impact of flexibility in choosing dependent variables, sample size, covariates, and reporting subsets of experimental 
conditions on the likelihood of encountering false positives. 

In this project, we run simulations for situations A, B, C, D, and combinations of each situations.


# Simulation 
For all the situations we simulated, we run 15,000 simulations with samples size of 20, under significance level of p < 0.05. 
We generate random samples from gaussian distributions.

| Situations                                                                  | Code File                            | Our Simulations | Paper's Result |
|-----------------------------------------------------------------------------|--------------------------------------|-----------------|----------------|
| Situation A: two dependent variables (r = .50)                              | [situation_A.py](situation_A.py)     | 8.6%            | 9.5%           |   
| Situation B: addition of 10 more observationsper cell                       | [situation_B.py](situation_B.py)     | 7.3%            | 7.7%           |
| Situation C: controlling for gender or interaction of gender with treatment | [situation_C.py](situation_C.py)     | 10.6%           | 11.7%          |
| Situation D: dropping (or not dropping) one of three conditions             | [situation_D.py](situation_D.py)     | 11.8%           | 12.6%          |
| Combine Situations A and B                                                  | [combined_AB.py](combined_AB.py)     | 13.86%          | 14.4%          |
| Combine Situations A, B, and C                                              | [combined_ABC.py](combined_ABC.py)   | 27.73%          | 30.9%          |
| Combine Situations A, B, C, and D                                           | [combined_ABCD.py](combined_ABCD.py) | 41.68%          | 60.7%          |