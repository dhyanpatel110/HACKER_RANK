# Task:
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect occurs the 5th item inspection?

# Geometric Distribution = q ^ (n-1) * p
# The probability of failure of 1 trial q , where q = 1 - p

# Input data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 3 denotes decimal places (i.e., 1.234  format):
result = q ** (n - 1) * p
print(round(result, 3))
