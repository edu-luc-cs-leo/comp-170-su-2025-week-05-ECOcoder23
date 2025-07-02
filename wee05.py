foo = "Pathfinder"
bar = "Sidewinder"

def intersection(foo: str, bar: str) -> str | None: 
    i = 0
    result = ""
    while i < len(foo):
        if foo[i] in bar and foo[i] not in result:
            shared_character = foo[i]
            result = result + shared_character
        elif foo[i] in result:
            result += ""
        elif foo[i] not in bar: 
            result += ""
        i += 1 
    else:
        if i == len(foo) and foo[-1] not in bar:
            result = None
    return result 

print(intersection(foo, bar))


string = "Amor"

def is_alphabetical(string: str) -> bool: 
   letter_range_1 = range(65, 91)
   letter_range_2 = range(97, 123)
   for i in range(len(string)):
      if ord(string[i]) in letter_range_1 or ord(string[i]) in letter_range_2: 
        result = True 
      else:
        result = False
   return result 

print(is_alphabetical(string))


string = "Wild_Child >:)"

def letters_only(string: str) -> str: 
   result = ""
   letter_range_1 = range(65, 91)
   letter_range_2 = range(97, 123)
   i = 0
   while i < len(string):
     if ord(string[i]) in letter_range_1 or ord(string[i]) in letter_range_2:
       result += string[i]
     else:
       result += ""
     i += 1  
   return result 

print(letters_only(string))
           

string = "Oblongata"

def generate_palindrome(string: str) -> str | None: 
   vowels = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
   string = letters_only(string)
   string_list = list(string)
   for letters in string:
      if ord(string[-1]) in vowels:
        mirror = string_list[-2::-1] 
      else:
         if ord(string[-1]) not in vowels:  
          mirror = string_list[::-1] 
      new_string_list = string_list + mirror 
      palin_str = "".join(new_string_list)
   return palin_str 

print(generate_palindrome(string))
      


def lower_case(string: str) -> str | None:
   upper_case = range(65,91)       
   result = ""
   string = letters_only(string)
   for i in range(len(string)):
      str_char = string[i]
      str_ascii = ord(string[i])
      if str_ascii in upper_case:
         new_str_ascii = str_ascii + 32
         new_str_char = chr(new_str_ascii)
      else: 
         if str_ascii not in upper_case:
            new_str_char = str_char
      result += new_str_char 
   return result

def is_palindrome(string: str) -> str | None: 
   string = lower_case(string)
   for letters in string:
      char_count = len(string)
      half_count = len(string)//2
      if char_count > 0 and char_count % 2 == 0:
         first_half_split = string[0:half_count:1]
         second_half_split = string[char_count:(half_count - 1):-1]
      elif char_count > 0 and char_count % 2 != 0:
         first_half_split = string[0:(half_count + 1):1]
         second_half_split = string[char_count:(half_count - 1):-1]
   else: 
      if char_count == 0: 
         first_half_split != second_half_split
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
