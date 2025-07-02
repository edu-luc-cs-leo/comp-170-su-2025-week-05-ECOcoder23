foo = "Pathfinder"
bar = "Sidewinder"

def intersection(foo: str, bar: str) -> str | None: 
    i = 0
    # Creates an empy string with variable name "result"
    result = ""
    while i < len(foo):
    # Finds if character is present in both strings and not 
    # already present in "result"
        if foo[i] in bar and foo[i] not in result:
            shared_character = foo[i]
    # If previous conditions = True, character is concatenated to "result"       
            result = result + shared_character
    # If previous conditions = False, nothing is concatenated 
        elif foo[i] in result:
            result += ""       
        elif foo[i] not in bar: 
            result += ""
    # Moves on to character number n + 1 in string   
        i += 1 
   
    # If no overlap between the strings exists, returns "None"
    else:
        if i == len(foo) and foo[-1] not in bar:
            result = None
    return result 

print(intersection(foo, bar))


string = "Amor"

def is_alphabetical(string: str) -> bool: 
# Creates two ranges with ASCII values of alphabetical characters   
   letter_range_1 = range(65, 91)
   letter_range_2 = range(97, 123)
   for i in range(len(string)):
# If character in string has ASCII value in either range, "result" = True  
      if ord(string[i]) in letter_range_1 or ord(string[i]) in letter_range_2: 
        result = True 
# If previous condition not met, "result" = False
      else:
        result = False
   return result 

print(is_alphabetical(string))


string = "Wild_Child >:)"

def letters_only(string: str) -> str: 
# Creates an empty string named "result"  
   result = ""
# Creates two ranges with ASCII values of alphabetical characters
   letter_range_1 = range(65, 91)
   letter_range_2 = range(97, 123)
   i = 0
   while i < len(string):
# If character in string has ASCII value in either range, it is concatenated to "result"    
     if ord(string[i]) in letter_range_1 or ord(string[i]) in letter_range_2:
       result += string[i]
# If character not in either range, nothing is concatenated 
     else:
       result += ""
# Moves on to character number n + 1 in string    
     i += 1  
   return result 

print(letters_only(string))
           

string = "Oblongata"

def generate_palindrome(string: str) -> str | None: 
# Creates a list named "vowels" with ASCII values of all vowels in alphabet    
   vowels = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
# Uses function "letters_only" to convert string characters to letters
   string = letters_only(string)
# Creates a list using characters from input string
   string_list = list(string)
   for letters in string:
# Checks if last character of string is in "vowels"
      if ord(string[-1]) in vowels:
# If previous condition met, a new list, "mirror", is created
# which mirrors the previous list from its second to last item      
        mirror = string_list[-2::-1] 
# If last character of string not in "vowels", a new list, "mirror"
# is created that mirrors the previous one from it's last item
      else:
         if ord(string[-1]) not in vowels:  
          mirror = string_list[::-1] 
# The first list of string characters is concatenated with the new list "mirror"
      new_string_list = string_list + mirror 
# The resultant list of the concatenation is turned into a string      
      palin_str = "".join(new_string_list)
   return palin_str 

print(generate_palindrome(string))
      


def lower_case(string: str) -> str | None:
# Creates a range of ASCII values for upper-case letters   
   upper_case = range(65,91)       
# Creates an empty string named "result"  
   result = ""
# Uses funtion "letters_only" to convert all string characters into letters   
   string = letters_only(string)
   for i in range(len(string)):
# If string character ASCII value in range "upper_case", the lowercase 
# equivalent is produced      
      str_char = string[i]
      str_ascii = ord(string[i])
      if str_ascii in upper_case:
         new_str_ascii = str_ascii + 32
         new_str_char = chr(new_str_ascii)
# If string character ASCII value not in range "upper_case", the 
# string character is conserved 
      else: 
         if str_ascii not in upper_case:
            new_str_char = str_char
# The lowercase characters and conserved characters are added to "result"
      result += new_str_char 
   return result

def is_palindrome(string: str) -> str | None: 
# All string characters converted to lowercase letters using function "lower_case"  
   string = lower_case(string)
   for char in string:
      char_count = len(string)
      half_count = len(string)//2
# Checks if the string isn't empty and has an even number of characters      
      if char_count > 0 and char_count % 2 == 0:
# Splits the string into two strings of equal length
         first_half_split = string[0:half_count:1]
         second_half_split = string[char_count:(half_count - 1):-1]
# Checks if the string isn't empty and has an odd number of characters
      elif char_count > 0 and char_count % 2 != 0:
# Splits the string into two strings of equal length, each including 
# the middle character        
         first_half_split = string[0:(half_count + 1):1]
         second_half_split = string[char_count:(half_count - 1):-1]
# If character count is equal to zero, the default output is false 
   else: 
      if char_count == 0: 
         first_half_split != second_half_split
# Compares whether the two strings made from the original are equivalent,
# and gives a boolean output (True or False)
   return first_half_split == second_half_split

  

      
      

   
        


     
   

























#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
