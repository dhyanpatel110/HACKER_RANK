'''
Task:
  Apply your knowledge of the .add() operation to help your friend Rupal.
  Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
  Find the total number of distinct country stamps.
  
Sample Input:
  7
  UK
  China
  USA
  France
  New Zealand
  UK
  France 
Sample Output:
  5
 '''
 
CODE:
  N = int(input())
  countries = set()
  for i in range(N):
      countries.add(input())
  print(len(countries))
  
  
  
  
  
