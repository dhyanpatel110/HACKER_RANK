'''
TASK:
  The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n , print i^2.

EXAMPLE:
  n = 5
  The list of non-negative integers that are less than n=5 is [0,1,2,3,4]. Print the square of each number on a separate line.
  0
  1
  4
  9
  16
'''

CODE:
  if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
        
        
        
        
        
