'''
Sample Input:
  ABCDEFGHIJKLIMNOQRSTUVWXYZ
  4
  
Sample Output:
  ABCD
  EFGH
  IJKL
  IMNO
  QRST
  UVWX
  YZ
'''

CODE:
  import textwrap
  def wrap(string, max_width):
    return textwrap.fill(string,max_width)

  if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
    
    
    
