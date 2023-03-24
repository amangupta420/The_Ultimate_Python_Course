print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# (-----------------------------------------------------------------   LENTH OF A STRING   -----------------------------------------------------------------)

# LENTH OF A STRING = We can find the lenth of the string using a functionn of python len() is known as lenth of the string.

name = ("aman, motu") # This is a variable.
print(len(name))      # This function of python named len() is used for counting the characters of the data of the variable.
# OUTPUT = 10 

fruit  = ("mango")   # This is a variable.
ag = len("fruit")    # This variable is counted the data of the variable (fruit) because here is used len() and we can use this variable anywhere as a shortcut.

print("mango is a", ag, " letter word." )

# OUTPUT = mango is a 5 letter word. 

fruit = ("mango")    # This is a variable.
mango = len("fruit") # Here I am using len for counting the data of variable (fruit). 

print(mango)         # Printing the variable mango.

# OUTPUT = Finally I got the output is 10.

print("----------------------------------------------------------------- SLICING ---------------------------------------------------------------------")
# SLICING = Slicing in Python is a Process through Which we can Divide a String, List etc in many Different Parts. [Same Like Cutting an Apple]

print(fruit[0:5])    # Printing the 'mango'

# [x:5] if x is empty then python will replace it with a 0.
print(fruit[0:4]) # Including 0 but not 4. 
print(fruit[0:3]) #  Including 0 but not 3.
print(fruit[ :2])
print(fruit[0:1])

# [0:x] if x is empty here then python will replace it with -1(length of the string)
print(fruit[0: ])

print("-------------------------------------------------------------- NEGATIVE SLICING ----------------------------------------------------------------")
# NAGATIVE SLICING = Nagative Slicing is Same like Slicing but it is done with negative words.
"""
Python Counts Nagative Words from end of the String or List.
Exp :- "Aman"
    -1 = 4
    -2 = 3
    -3 = 2
    -4 = 1
    -5 = 0
"""
veg = ("potato")
potato = len("veg")

print(veg[0:  ])
print(veg[0:-1])
print(veg[0:-2])
print(veg[0:-3])
print(veg[0:-4])
print(veg[0:-5])
print(veg[0:-6])

print("-------------------------------------------------------------- QUICK QUIZ  ----------------------------------------------------------------")

nm = ("harry")
print(nm[-4:-2])

# OUTPUT= ar

print("---------------------------------------------------------  LOOP THROUGH A STRING  ---------------------------------------------------------")
# LOOP THROUGH A STRING = Strings are arrays and arrays are iterible. Thus we can loop thrugh strings.

