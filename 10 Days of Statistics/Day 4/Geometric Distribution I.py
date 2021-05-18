# Task:
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect occurs the 5th item inspection?

# The probability of failure of 1 trial q , where q = 1 - p

# Input data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = q ** (n - 1) * p
print(round(result, 3))
