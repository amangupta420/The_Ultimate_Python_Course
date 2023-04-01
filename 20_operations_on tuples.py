print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-----------------------------------------------------------   MANIPULATING TUPLES   ---------------------------------------------------------------------")
# MANIPULATING TUPLES = Tuples are immutable.If you want to change or add in tuple then first convert tuple to a list then  perform operation that list then convert it back to tuple.

countries = ("spain","italy","india","england","germany") # This is a tuple.
print(type(countries))  # This is the method of  checking class.
print(countries) # Printing a tuple.
temp = list(countries)  # Converting a tuple into a list.
print(temp) # Printing a list.
temp.append("russia")  # Adding item into a list temp.
temp.pop(3)    # Removing item in a list temp.
temp[2] = "golden bird"  #Changing item in a list.
country = tuple(temp) # Converting a list into a tuple.
print(country) 

print("--------------------------------------------------------   CONCATINATING TWO TUPLES   ---------------------------------------------------------------------")

veg = ("potato","tomato","ladyFinger","carrot","onian")  # This is the tuple of vegetables.
fruit = ("apple","banana","grapes","kiwi","pineApple")   # This is the tuple of fruits. 
mixItem = veg + fruit  # Merging veg and fruit into a variable mixItem.
print(mixItem)  # Printing mixItem.

print("-------------------------------------------------------------   TUPLE METHODS  ---------------------------------------------------------------------")
# TUPLES METHOD =  As tuple is immutable type of collection of elements it have limited buuiltin methods.

# This is the first method.
num = (1, 2, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 1, 2, 4, 2, 1)  # This is the tuple of numbers.  
print(num.count(1))

# This is the second method.
num = (1, 2, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 1, 2, 4, 2, 1) 
total = (num.count(4))
print("count of 4 in tuples is:",total)

print("-------------------------------------------------------------   INDEX METHODS  ---------------------------------------------------------------------")
# INDEX METHODS = The index() method returns first occursnce of the given element from the tuple.

# This is the first method.
nums =  (1, 2, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 1, 2, 4, 2, 1)
print(nums.index(5))

# This is the second method.
nums =  (1, 2, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 1, 2, 4, 2, 1)
number = (nums.index(6))
print("THe index of 6 is:",number)

# This is the method of indexing in middle.
nums =  (1, 2, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 1, 2, 4, 2, 1)
number = (nums.index(4,6,11)) 
print("THe index of 4 is:",number)

print("-------------------------------------------------------------   LENGTH METHODS  ---------------------------------------------------------------------")

nums =  (1, 2, 3, 4, 5, 6, 6, 5, 4, 4, 3, 2, 1, 2, 4, 2, 1)
print(len(nums))

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")