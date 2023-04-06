print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("------------------------------------------------------------------   SETS   ---------------------------------------------------------------------")
# SETS = The sets are unorderd collection of data items. They store multiple items in single curly braket. set is unchangable.

s = {7,5,6,9,7,5,6,9,}  # In this variable.Some values are repeated but but set is checked it and deleted those values which value is repeated. But this is unordered collection. 
print(s)
info = {"aman",5,7,6,7,5,False,5.6,5.6}  # Set is able to store more type of values.
print(info)

print("---------------------------------------------------------------   QUICK QUIZ   ---------------------------------------------------------------------")

# CREATE AN EMPTY SET OF AMAN GUPTA.
amanGupta = {}  # We think the question is empty set then make a amanGupta variable and leave it empty. but the answer is class dictionary now you think but i maked a set but in output showing the claas dict. Why? Because this is wrong.
print(type(amanGupta))

# Now the right is given below.
amanGupta = set()
print(type(amanGupta))

print("--------------------------------------------------------------   ACCESSING ITEMS   ---------------------------------------------------------------------")

for value in info:
    print(value)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")