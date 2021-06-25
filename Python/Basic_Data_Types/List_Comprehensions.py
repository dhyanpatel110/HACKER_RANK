EXAMPLE:
  x = 1
  y = 1
  z = 1
  n = 2
  [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


CODE:
  if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Will store the list for the cuboid
    cuboid = []
    
    # Various loops that will go through all of the possible
    # coordinates given by x, y, and z.
    for i in range(x+1):
        for j in range(y+1):
                for k in range(z+1):
                    # The sum of i, j, and k cannot be equal to n.
                    if( ( i + j + k ) != n ):
                        # Creates a temporary list and adds it cuboid list.
                        tmp = [i, j, k]
                        cuboid.append(tmp)
    # Prints the cuboid list.                   
    print( cuboid )
    
    
    
    
