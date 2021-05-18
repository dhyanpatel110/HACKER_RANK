# Task:
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the first 5 inspections?

# Input data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (q ** (i - 1) * p)

        
# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 3 denotes decimal places (i.e., 1.234  format):
print(round(result, 3))


