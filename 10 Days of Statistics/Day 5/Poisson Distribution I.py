# SOME BASIC CONSTANT AND MASS  FUNCTION OF POISSION DISTRIBUTION
# e is Euler's number (e = 2.71828...)
# f(k, lambda) = lambda^k * e^-lambda / k!

# Task:
# A random variable, X , follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.


# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

# Input data
lam = float(input())
k = float(input())
e = 2.71828

# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 3 denotes decimal places (i.e., 1.234  format):
result = ((lam ** k) * (e ** -lam)) /  factorial(k)
print(round(result, 3))

