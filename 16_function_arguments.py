print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("------------------------------------------------------------   ARGUMENTS FUNCTION   ---------------------------------------------------------------------")

def average(a, b):
    print("The average is ", (a+b)/2)
average(4, 6)

print("------------------------------------------------------------  DEFAULT ARGUMENTS   ---------------------------------------------------------------------")
# DEFAULT ARGUMENTS = A default argument is an argument that assumes a default if a value not given in the function call for the argument.

def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average(a=9) # The value of b is not given then python interpreter take it as default value.


def name(fname, mname = "murli",lname = "praduymn"):
    print("hello,", fname, mname, lname)
name("aman",)

def grocery(item, price=40.00):   # To display the given arguments.
    print('Item = %s' % item)     
    print('Price = %.2f' % price)

grocery(item='Sugar', price=50.75)# Pass two arguments.
grocery(item='Sugar')             # Default for price is used.

print("------------------------------------------------------------ KEYWORD  ARGUMENTS   ---------------------------------------------------------------------")
# KEYWORD  ARGUMENTS = We can provide the arguments with key = value, This way the interpreter recognises the arguments by the parameter name.

def fruit(apple=100, banana=90):
    print("Total rate of fruit is: ", apple+banana)

fruit(banana=60, apple=70)

print("------------------------------------------------------------ REQUIRED  ARGUMENTS   ---------------------------------------------------------------------")
# REQUIRED  ARGUMENTS = Which value is required for provied is called required arguments.

def average(a, b, c=12,):
    print("The average is ", (a+b+c)/2)
average(a=9, b=1,) # The value of a and b is provied because he is no default value and this is required value.

print("------------------------------------------------------- VARIABLE LENGTH  ARGUMENTS   ---------------------------------------------------------------------")
 
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is: ", sum/len(numbers))
c = average(5,10,15,20)
print(c)

print("------------------------------------------------------------ RETURN  ARGUMENTS   ---------------------------------------------------------------------")
# RETURN  ARGUMENTS = The return statement is used to return the value of the expression back to the calling function.

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)
c = average(5,10,15,20)
print(c)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")