# Task:
# The number of tickets purchased by each student for the
# University X vs. University Y football game follows a distribution that has a mean of u = 2.4 and a standard deviation of 2.0
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. 
# If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

# THIS IS STATIC CODE

# Import library
import math

# Define functions
# The math.erf() method returns the error function of a number (find positive and negative number)
# The math.sqrt() method returns the square root of a number.
def cdf(std_dev, avg, x):
    inner = 1 + math.erf((x - avg) / (std_dev * math.sqrt(2)))
    return inner * 0.5

# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 4 denotes decimal places (i.e., 1.2345  format):  
ans = cdf(math.sqrt(100) * 2.0, 100 * 2.4, 250)
print (round(ans, 4))




