#TASK:
  Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).

#CODE:
  if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # The tuple() function converts a list to a tuple.
    t = tuple(integer_list)
            
    # Prints the result of the hash function with parameter t.
    print( hash(t) )

    
    
    
    
