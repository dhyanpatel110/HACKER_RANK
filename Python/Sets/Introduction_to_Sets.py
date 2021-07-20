'''
Explanation:
  Here, set[154,161,167,170,171,174,176,182]is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.
  average = 1355/8 = 169.375
'''
CODE:
  def average(array):
    # your code goes here

    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output;

 if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
    
    
    
