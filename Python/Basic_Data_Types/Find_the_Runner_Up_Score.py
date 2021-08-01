'''
EXPLANATION:
 Given list is [2,3,6,6,5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

CODE:
 if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Checks if n is in between 2 and 10.
    if( 2 <= n <= 10  ):
        # Removes all the duplicates in the list.
        tmp = list( set( arr ) )
        
        # Removes the highest number
        tmp.remove( max( tmp ) )
        
        # Prints the next highest number.
        print( max( tmp ) )
        
        
        
        
