TASK:
  The provided code stub reads two integers, a and b, from STDIN.
  Add logic to print two lines. The first line should contain the result of integer division, a//b . The second line should contain the result of float division, a/b .


EXPLANATION:
  a = 3
  b = 5
  The result of the integer division 3//5 = 0
  The result of the float division is 3/5 = 0.6
  
  
CODE:
  if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
    
    
    
    