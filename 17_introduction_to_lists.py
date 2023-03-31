print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("------------------------------------------------------------------   LISTS   ---------------------------------------------------------------------")
# LISTS = A list is similar to an array that consists of a group of elements or items.

marks = [1,4,8,12,16,20]  # 6 childrens were read in one school.This is his marks.
print(marks)              # Printing the marks of childrens.
print(type(marks))        # This is the way of finding what is the type of variable. LIKE AS: list(), dict (), tuple(), etc.

print("----------------------------------------------------------------   LISTS INDEX   ---------------------------------------------------------------------")
#LISTS INDEX =  We can access part of string by using this index which starts from 0.square Brakets can be used for access element of the string.

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
"""
square Brakets can be used for access element of the string.
"""

print("----------------------------------------------------------------   POSITIVE INDEX   ---------------------------------------------------------------------")
# POSITIVE INDEX = As we have seen that lists item have index, As we can access items using these indexes.

color = ["red", "yellow", "blue", "black", "green", "pink", "purple"]
#         [0]      [1]      [2]     [3]       [4]     [5]      [6].

print(color[0])
print(color[3])
print(color[6])

print("----------------------------------------------------------------   NEGATIVE INDEX   ---------------------------------------------------------------------")
# NEGATIVE INDEX =  Negative indexing is also access item but from the end of the list. The last item has index[-1]and second last item has index[-2]. 

color = ["red", "yellow", "blue", "black", "green", "pink", "purple"]
#         [0]      [1]      [2]     [3]       [4]     [5]      [6].

print(color[-6]) 
print(color[len(color)-6])  
print(color[7-6])
print(color[1])
 
# Check whether an item in present in the list?
"""
We can check if a given item in present in the list. This is done using in keyword.
"""
if "red" in color:
    print("yes")
else:
    print("no")

if "black" in color:
    print("yes")
else:
    print("no")

