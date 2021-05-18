# Task:
# The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
# The daily cost of operating A is C = 160 + 40X².
# The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
# The daily cost of operating B is C = 128 + 40Y².

# Input data
lambdas = list(map(float, input().split()))
lambda_a = lambdas[0]
lambda_b = lambdas[1]

# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 3 denotes decimal places (i.e., 1.234  format):
print (round(160 + 40 * (lambda_a + lambda_a ** 2), 3))
print (round(128 + 40 * (lambda_b + lambda_b ** 2), 3))
