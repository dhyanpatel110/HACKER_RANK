# Task:
# A large elevator can transport a maximum of 9800 pounds. 
# Suppose a load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean of u = 205 pounds and a standard deviation of a = 15 pounds. 
# Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

# Import library
import math

# Define functions
# The math.erf() method returns the error function of a number (find positive and negative number)
# The math.sqrt() method returns the square root of a number.
def cumulative(avg, std_dev, x):
    inner = 1 + math.erf((x - avg) / (std_dev * math.sqrt(2)))
    return 0.5 * inner

# Input data
max_weight = float(input())
num_boxes = float(input())
avg = float(input())
std_dev = float(input())

sample_avg = num_boxes * avg
sample_std_dev = math.sqrt(num_boxes) * std_dev

# We can show result on the screen
# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# 4 denotes decimal places (i.e., 1.2345  format):
ans = cumulative(num_boxes * avg, math.sqrt(num_boxes) * std_dev, 9800)
print (round(ans, 4))




