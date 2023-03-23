print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#  (---------------------------------------------------------------      DATA TYPECASTING     --------------------------------------------------------------)-

# TYPECASTING = When any data type change in other data type is known as data typecasting in python.
# FUNCTION AND METHODS = Python sopports a wide variety of functions or methods like as: tuple, dict, str, float, hex, list etc.

# Giving data in variable (a).
a = "5"

# Giving data in variable (b).
b = "10"

# Printing Some of a+b (Expected = 15)
print(a + b) # Output = "510"

"""
So as You Can see that The Result is not Same as we Expected
The Reason Behing This is That 
According to Python Both a and b are Strings Not Inteagers so Python is Concatinating thease String and This is True Behaviour for Python.
"""


print(int(a) + int(b))
"""
If I want to add the data of variable then I will use a funtion of python (int) which is able
to convert string in integer and data is must be a valid integer.like as: 2,3,4,5,6 etc.
"""

"""
There are two types of typecasting.
01. EXPLICIT TYPECSTING.
02. IMPLICIT TYPECSTING.

"""

# (-------------------------------------------------------      EXPLICIT TYPECASTING       ---------------------------------------------------------------)

# EXPLICIT TYPYECASTING  = When any data type change in other data type according to a programmer or via devoloper according to his requirments is known as explicit typecasting.

string = "15"
number =  7
string_number = int(string)  #  If string is not a valid integer then you gets error after run the python file.
sum = number + string_number 
print("The sum of the both numbers is:", sum )

potato = "50"  
tomato = "40"
ladyfinger = 60 
potato = int(potato) #   If string is not a valid integer then you gets error after run the python file.
tomato = int(tomato) #   If string is not a valid integer then you gets error after run the python file.
totalRate = ladyfinger + potato + tomato
print("The total rate of the vegetables is:", totalRate)

#  ------------------------------------------------------      IMPLICIT TYPECASTING       ------------------------------------------------------------)
"""
- IMPLICIT TYPECASTING  = Data types in python do not have same level. some of the data types have higher order and some data types have lower order and 
    Python convert automatically the lower to higher is called known as implicit typecasting.
- Lower Order = Lower Order in Python Means that a Datatype Which cannot contain other datatypes value in it. Exp: Inteager.
- Higher Order = Higher Order in Pythobn Means that a Datatype Which can contain other datatypes values in it. 
    Exp: Float(Because it can contain both Inteager and Float Values: 1.0 = 1)
"""

c = 1.5  # This is float. 
d = 9    # This is integer.

print(c + d) # When I want to add the C and D then python auto converted the integer in float.

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")