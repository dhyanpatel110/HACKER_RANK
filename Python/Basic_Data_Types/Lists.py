EXAMPLE:
  N = 4
  append 1
  append 2
  insert 3 1
  
  print
  append 1: Append 1 to the list arr = [1]
  append 2: Append 2 to the list arr = [1,2]
  insert 3 1: Insert 3 at index 1 arr = [1,3,2]
  
  Output:
  [1,3,2]
  

CODE:  
  # Lists in Python - Hacker Rank Solution
  if __name__ == '__main__':
      N = int(input())
      # Lists in Python - Hacker Rank Solution START
      Output = [];
      for i in range(0,N):
          ip = input().split();
          if ip[0] == "print":
              print(Output)
          elif ip[0] == "insert":
              Output.insert(int(ip[1]),int(ip[2]))
          elif ip[0] == "remove":
              Output.remove(int(ip[1]))
          elif ip[0] == "pop":
              Output.pop();
          elif ip[0] == "append":
              Output.append(int(ip[1]))
          elif ip[0] == "sort":
              Output.sort();   
          else:
              Output.reverse();
              
              
              
              
              
  
