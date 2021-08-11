'''
Sample Input:
  Ross
  Taylor
Sample Output:
  Hello Ross Taylor! You just delved into python. 
Explanation:
  The input read by the program is stored as a string data type. A string is a collection of characters.
'''

#CODE:
  def print_full_name(a, b):
    b = b+"!"
    print("Hello",a, b,"You just delved into python.");
    
  if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
    
    
    
    
