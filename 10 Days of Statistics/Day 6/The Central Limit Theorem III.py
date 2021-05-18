# Confidence interval

# Task:
# You have a sample of 100 values from a population with mean u = 500 and with standard deviation a = 80. 
# Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A < x < B) = 0.95. 
# Use the value of z = 1.96. 
# Note that z is the z-score.

# Import library
import math

# Input data
n = float(input())
mean = float(input())
std = float(input())
percent_ci = float(input())
value_ci = float(input())

# Formula  of CI (Confidence interval)
# The math.sqrt() method returns the square root of a number.
ci = value_ci * (std / math.sqrt(n))

# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 2 denotes decimal places (i.e., 1.23  format):
print(round(mean - ci, 2))
print(round(mean + ci, 2))
