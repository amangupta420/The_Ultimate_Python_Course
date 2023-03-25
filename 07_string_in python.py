print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# (--------------------------------------------------------------------    STRINGS   ----------------------------------------------------------------------)

# STRINGS = Any textual data under in double or single code is known as string. strings are used when working unicode character.

name = "Aman Gupta "        # This is double code string.

friend = "Praduyman Yadav " # This is double code string.

otherFriend = 'motu '       # This is single code string.

apple ="""
hey, aman 
how are you 
I want to eat an apple.
"""

print("hello," + name )

print(apple)

# (--------------------------------------------------------------    MULTILINE STRINGS   ----------------------------------------------------------------)

# MULTILINE STRINGS = We will use the multiline strings while printing big paragraphs.

st = """

Hello, Harry

Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience
"""

str = '''
Hello, Harry

Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience
'''

# This is multiline strings. we will use the multiline strings while printing big paragraphs.
 
print(st)

print(str)

# (---------------------------------------------------   ACCESSING CHARACTERS OF THE STRING   ----------------------------------------------------------)

"""
ACCESSING CHARACTERS OF THE STRING = Strings is like an array of characters. We can access part of string by using its index which starts from 0.
Square Brakets can be used for access element of the string.
"""

print(otherFriend[0])

print(otherFriend[1])

print(otherFriend[2])

print(otherFriend[3])

print(otherFriend[4])

# print(otherFriend[5])  #  This print is throws an error because the data of variable is only 0 to 4 characters. If you will printing the more
                       #  charactyers to data then he throws an error.

# (----------------------------------------------------    LOOPING THROUGH THE STRINGS   -----------------------------------------------------------------)

# LOOP = We can loop through strings  using a for loop laike this:
  
for character in str:
  
  print(character)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")