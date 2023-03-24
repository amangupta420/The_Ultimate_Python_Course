print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-------------------------------------------------------------   STRINGS METHODS  ----------------------------------------------------------------------")

# STRING METHOD = Python provides a built in methods that we can usw to after and modify the strings.

print("------------------------------------------------------------------   UPPER  ----------------------------------------------------------------------")
# UPPER = This method is used for convert the strings in upper case.

a = "!!! Aman !!! !!! !!! !!! !!!"       # This is variable.
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

str1 = ("heLlo")
hello = str1.capitalize() 
print(hello)
str2 = ("hello wOrLLd")
helloWorld = str2.capitalize()
print(helloWorld)

print("----------------------------------------------------------------   CENTER   ----------------------------------------------------------------------")
# CENTER = This center() method aligns the string to the center as per the parameters given by the user.

