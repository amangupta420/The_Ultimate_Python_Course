print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# INPUT = We can take user input directly by input() Function This input function gives a return value as string character hence we have to pass that into a variable to store it.

a = input("enter your name:")
print("my name is", a)

x = input("Enter your first number: ")
y = input("Enter your second number: ")

# print(x + y)
"""
If The First Number Entered by You is: 12.
And the Second Number Entered by You is: 88.
Then output will be: 1288.
Because we learned in previous chapter That python is able to add integers not strings and our input is in a string so python interpreter is not able to add the string. 
"""

print(int(x)  +  int(y))

"""
Now :-
If The First Number Entered by You is: 12.
And The Second Number Entered by You is: 88.
Then output will be: 100
so we use a built in python function int()
"""
# You can also use many different types of operators.

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
