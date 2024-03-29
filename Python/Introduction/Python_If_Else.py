'''
TASK:
  Given an integer,n, perform the following conditional actions:

  If n is odd, print Weird
  If n is even and in the inclusive range of 2 to 5, print Not Weird
  If n is even and in the inclusive range of 6 to 20, print Weird
  If n is even and greater than 20, print Not Weird

EXPLANATION:
  n = 24
  n > 20 and n is even, so it is not weird.
'''

CODE:
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}

    print(check[
         n%2==0 and (
             n in range(2,6) or 
            n > 20)
         ])
    
    
    
    
    
