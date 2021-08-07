'''
EXAMPLE:
  records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
  The ordered list of scores is [20.0 , 50.0], so the second lowest score is 50.0. 
  There are two students with that score:["beta" , "alpha"] . Ordered alphabetically, the names are printed as:
  alpha
  beta
'''

CODE:
  # Will save the variables from the input.
  li = []
  # Will only save the scores from the input.
  scores = []

  for _ in range(int(input())):
      name = input()
      score = float(input())
    
      # Temporary list that will put the variables together.
      tmp = [ name, score ]
      # Appends the temporary list to the li list.
      li.append(tmp)
      # Appends the score to the scores list.
      scores.append(score)

  # Remove duplicate scores.
  uniqueScores = list(set(scores))
  # Sorts the scores from low to high.
  uniqueScores.sort()
  # Saves the second lowest score into a variables.
  # Since there are no duplicates, the second lowest grade should be
  # the second item in the list.
  secondLowest = uniqueScores[1]

  # Sorts the li list in alphabetical order.
  li.sort()

  # This loop  goes through all of the items.
  for i in li:
      # If the score is the same as the second lowest, we print the name.
      if( i[1] == secondLowest ):
          print( i[0] )

          
          
          
          
