print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#  INPUT = We can take user input directly by input() Function This input function gives a return value as string/character hence we have to pass that into a variable.

a = input("enter your name:")
print("my name is", a)

x = input("Enter your first number: ")
y = input("Enter your second number: ")

# print(x + y) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
If you entered your first number is: 12.
And you entered your second number is: 88.
Then output is: 1288.
Because we learned in previous chapter python able to add integers not strings and our input is in string so python interpreter not able to add the string. 

"""

print(int(x)  +  int(y))

"""
If you entered your first number is: 12.
And you entered your second number is: 88.
so we use a python function int()
Then output is  100
"""
# You can also use many types of opreters.

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
