print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-------------------------------------------------------------   STRINGS METHODS  ----------------------------------------------------------------------")

# STRING METHOD = Python provides a built in methods that we can usw to after and modify the strings.

print("------------------------------------------------------------------   UPPER  ----------------------------------------------------------------------")
# UPPER = This method is used for convert the strings in upper case.

a = "!!! Aman !!! Aman !!! Aman !!! Aman !!!"       # This is variable.
print(len(a))    # Printing lenght of variable(a).
print(a.upper()) # Printing lenght of variable in upper case use of apython function upper(). 

print("------------------------------------------------------------------   LOWER  ----------------------------------------------------------------------")
# LOWER = This function is used to convert the strings in lower case.

print(a.lower())

print("------------------------------------------------------------------   RSTRIP  ----------------------------------------------------------------------")
# RSTRIP = This function is used for deleting other characters in string or variable.

print( a.rstrip("!")) 

print("------------------------------------------------------------------   REPLACE  ----------------------------------------------------------------------")
# REPLACE = Replace function is used for replacing data in variable like as:

print(a.replace("Aman", "motu"))

print("------------------------------------------------------------------   SPLIT  ----------------------------------------------------------------------")
# SPLIT = Spilt is used for converting any text in list.

print(a.split(" ")) 

print("----------------------------------------------------------------   CAPITALIZE  ----------------------------------------------------------------------")
# CAPITALIZE = Capitalize method is used for turning in capital letter of our blogheadings.

blogheading = ("introduction tO my nEw propeRty")
print(blogheading.capitalize())

str1 = ("heLlo hello hello hello")
hello = str1.capitalize() 
print(hello)
str2 = ("hello wOrLLd")
helloWorld = str2.capitalize()
print(helloWorld)

print("----------------------------------------------------------------   CENTER   ----------------------------------------------------------------------")
# CENTER = This center() method aligns the string to the center as per the parameters given by the user.

str3 = "Welcome to the console!!!"
print(len(str3))
print(len(str3.center(50)))

str4 = "Welcome to the terminal!!!"
print(str4.center(50,"."))

print("----------------------------------------------------------------    COUNT    ----------------------------------------------------------------------")
# COUNT = Count function is use for counting the sme name in any strings or variables.

print(a.count("Aman"))
print(str1.count("hello"))

str5 = "jkhkahkjahkgaaghaagjhaa"
countstr5 = (str5.count("a"))
print(countstr5)

print("---------------------------------------------------------------    ENDSWITH    ----------------------------------------------------------------------")
# ENDSWITH = The endswith method checks. If the string ends with a given value. If yes then return true, else return false.

str6 = "Welcome to the console"
print(str6.endswith("!!"))
print(str6.endswith("to",4, 10)) # we can even also check for a value in between a string by providing start and end index positions.

print("-----------------------------------------------------------------    FIND    ----------------------------------------------------------------------")
# Find = The find method searches for the first occurence of the given value and returns the index where it is present. If given value is absent from sting then return -1.

str7 = "he's name is aman. he is an honest man."
print(str7.find("aman"))
print(str7.find("amanGupta"))  # If you are which value is given in index then he is not present in data of the variable then find return -1.

print("----------------------------------------------------------------    INDEX    ----------------------------------------------------------------------")
# INDEX = Index is same as the find method which is searches for the first occurence of the given value and return the index where it is prsent .If given value is absent from stiring then python throws an errror.

Str8 = "he's name is aman. he is a simple and silent boy."
print(Str8.index("aman"))
#  NOW:
# print(Str8.index("amanGupta")) # If you are which value is given in index then he is not present in data of the variable then python throws an error. 

print("---------------------------------------------------------------    ISALNUM    ----------------------------------------------------------------------")
# ISALNUM = The isalnum method returns true only if the intire string only consist of A-Z a-z 0-9. If any other charecters or punctuation presnt then it return false.

str9 = "Wellcome to my new haveli no.135"
print(str9.isalnum()) # Printing the str9 for checking the data of the variable is allphanumeric or not, Use to method of python isalnum() and out put is comming false the this str9 is alphanumeric.
#  NOW:
str9 = "Wellcometomaynewhavelino135"
print(str9.isalnum()) # Printing the str9 for checking the data of the variable is allphanumeric or not, Use to method of python isalnum() and out put is comming ture the this str9 is alphanumeric.

print("---------------------------------------------------------------    ISALPHA    ----------------------------------------------------------------------")
# ISALPHA = The isalpha() is too same as the isalnum() only one diffrent in isalpha to isalnum. In isalnum read all characters like as:A-Z, a-z, 0-9. but isalpha read only A-Z, a-z.
str10 = "Wellcometomynewhaveland135"
print(str10.isalpha())  # In the data of the variable is added integer so output is comming false.
#  NOW:
str10 = "Wellcometomynewland"
print(str10.isalpha())  # In the data of the variable is not integer so output is comming true.

print("---------------------------------------------------------------    ISLOWER    ----------------------------------------------------------------------")
# ISLOWER = The islower method use for check all the words in the value is lower or not.

substr1 = "Wellcome To Mmy New Company Which Is Growth By Your Bless"
print(substr1.islower()) # Its output is comming false because the value of the variable is in capital word.
#  NOW: 
substr2 = "wellcome to my new company which is growth by your bless"
print(substr2.islower()) #  Its output is comming true because the value of the variable is in smsll word.
 
print("--------------------------------------------------------------    ISPRINTABLE    ----------------------------------------------------------------------")
# ISPRINTABLE = This isprintable method is used for checking characters which is printable and not printable.

substr3 = "wellcome to my new company\n"
print(substr3.isprintable()) # Its output is comming false so this is not printable because in value added backslashn(\n).
# NOW:
substr3 = "wellcome to my new company"
print(substr3.isprintable()) # Its output is comming true so this is not printable because all these values are printable.

print("----------------------------------------------------------------    ISSPACE    ----------------------------------------------------------------------")
# ISSPACE = This method is tells about space if in value have no space then will returns false and in value have spaces then ti returns true.

substr4 = "wellcome to my new lorry" # Here output is false.
print(substr4.isspace())
# NOW:
substr4 = "                        " # Here output is true.
print(substr4.isspace())

print("----------------------------------------------------------------    ISTITLE    ----------------------------------------------------------------------")
# ISTITLE = The istitle method is use for checking the all word's first letter is capital or not.

substr5 = "World Health orgnization"
print(substr5.istitle()) # The output is comming false because the word's first letter is small.
# NOW:
substr5 = "World Health Orgnization"
print(substr5.istitle())    # The output is comming true because the word's first letter is capital. 

print("----------------------------------------------------------------    ISUPPER    ----------------------------------------------------------------------")
# ISUPPER = The isupper is exactlly same as islower. Difrence with each other is islower check the letters are small or not and isupper is check the letter is capital or not.

substr6 = "World Health orgnization"
print(substr6.isupper()) # In this word's letter are small then output is false.
# NOW:
substr6 = "WORLD HEALTH ORGNIZATION"
print(substr6.isupper())  # In this word's letter are capital then output is true.

print("---------------------------------------------------------------    STARTSWITH    ----------------------------------------------------------------------")

# STARTSWITH = This method is check which character you are given is starting in string or not.

substr7 = "Aman gupta is the writer of his luck"
print(substr7.startswith("murli")) # Here output is comming false because which character given is not starting in string.
substr7 = "Aman gupta is the writer of his luck"
print(substr7.startswith("Aman"))   # Here output is comming true because which character given is starting in string.

print("---------------------------------------------------------------    SWAPCASE    ----------------------------------------------------------------------")
# SWAPCASE = The swapcase method is changes the character casing of the string. upper case are converted lower case to upper caseupper case to lower cas.

substr8 = "AMAN GUPTA IS WRITER OF HIS LUCK"
print(substr8.swapcase()) # The character is capital letter but output is comming in small letters.
substr8 = "aman gupta is the writer of his luck"
print(substr8.swapcase()) # The character is small letter but output is comming in capital letters. 

print("----------------------------------------------------------------    TITLE    ----------------------------------------------------------------------")
# TITLE = The title method of capabilities each letter of the word within the string.

substr9 = "imagination is always beautiful"
print(substr9.title()) # The title method is converted the word's first letter in capital letter. This is very helpful in blogs etc.

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
