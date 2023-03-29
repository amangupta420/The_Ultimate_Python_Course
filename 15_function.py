print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("----------------------------------------------------------------   FUNCTION   ---------------------------------------------------------------------")
# FUNCTION = Function is similar to a program that consist of a group of statements that are intented to perform a specific task.

def calculateGmean(a, b): # Def is a function which indicate to python interpreter,s I am writing a function.
    mean = (a*b)/(a+b)
    print(mean)
a = 9 # a is variable.
b = 8 # b is variable.
def isGreater(a, b):      # This def function is used for short cut of finding who is greater.
    if(a>b):              # This if() is used for variable a, b. Who is greater a or b.
        print("First number is greater.")
    else:
        print("Second number is greater or equal.")

def islesser(a,b):  # This function is used for finding who is lesser a or b.
    pass            # It is indicates the python interpreter's do not excute this line.leave it. 

calculateGmean(a, b)      # This is a function which calculate means of two numbers.
# gmean1 = (a*b)/(a+b)
# print(gmean1)


c = 8 # c is variable.
d = 7 # d is variable.
isGreater(c, d)           # This function is used for short cut of finding who is greater.
calculateGmean(c, d)      # This is a function which calculate means of two numbers.
# if(c>d):
#     print("First number is greater.")
# else:
#     print("Second number is greater or equal.")

# gmean2 =(c*d)/(c+d)     # This is the method of calculate the mean of two numbers but If I want to find mean in my code 100 times then this is very larger so i will not using this method.
# print(gmean2)

print("-------------------------------------------------------------  BUILT IN FUNCTION   ---------------------------------------------------------------------")
# BUILT IN FUNCTION = Which function is already maded by other programmer is called built in function.
# LIKE AS: min(), max(), len(), sum(), type(), range(), list(), etc

print("-----------------------------------------------------------  USER DEFINED FUNCTION   ---------------------------------------------------------------------")
# USER DEFINED FUNCTION = When we write a function to run specfictasks per as our need is called user defined functions.
"""
LIKE AS:1 

def calculateGmean(a, b): 
    mean = (a*b)/(a+b)
    print(mean)

LIKE AS:2

 def isGreater(a, b):  
    if(a>b):              
        print("First number is greater.")
    else:
        print("Second number is greater or equal.")

"""

print("-----------------------------------------------------------  CALLING A FUNCTION   ---------------------------------------------------------------------")
# CALLING A FUNCTION =  We call a function by giving the function name.

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")