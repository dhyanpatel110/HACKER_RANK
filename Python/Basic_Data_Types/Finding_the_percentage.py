EXPLANATION:
  Marks key:value pairs are
    'alpha':[20,30,40]
    'beta':[30,50,70]
     query_name = 'beta'
     the query_name is 'beta'. 'beta' average score is (30+50+70)/3 = 50.0
 
  
CODE:
  # Finding the percentage in Python - Hacker Rank Solution
  if __name__ == '__main__':
      n = int(input())
      student_marks = {}
      for _ in range(n):
          name, *line = input().split()
          scores = list(map(float, line))
          student_marks[name] = scores
      query_name = input()

      # Finding the percentage in Python - Hacker Rank Solution START
      output = list(student_marks[query_name])
      per = sum(output)/len(output);
      print("%.2f" % per);
  
  
  
  
  
