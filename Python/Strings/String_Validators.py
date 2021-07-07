Task:
  You are given a string .
  Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
    str.isalnum():This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    str.isalpha():This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    str.isdigit():This method checks if all the characters of a string are digits (0-9).
    str.islower():This method checks if all the characters of a string are lowercase characters (a-z).
    str.isupper():This method checks if all the characters of a string are uppercase characters (A-Z).
      
      
CODE:
  if __name__ == '__main__':
    s = input()
    flag_alnum = False
    flag_alpha = False
    flag_digit = False
    flag_lower = False
    flag_upper = False
    for i in s:
        if i.isalnum():
            flag_alnum = True
        if i.isalpha():
            flag_alpha = True
        if i.isdigit():
            flag_digit = True
        if i.islower():
            flag_lower = True
        if i.isupper():
            flag_upper = True

    print(flag_alnum)
    print(flag_alpha)
    print(flag_digit)
    print(flag_lower)
    print(flag_upper)
    
    
    
    
    
