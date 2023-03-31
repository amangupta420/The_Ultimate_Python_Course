print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("--------------------------------------------------------------   LISTS METHODS   ---------------------------------------------------------------------")

# append().
l = [2, 6, 1, 2, 1, 1, 8, 78, 34, 45, 3,] # This is list of some numbers.
print(l)   
l.append(200)  # This l.append() is a method of list. This list is used for adding other element in list. 
print(l)

# sort().
l.sort() # This l.sort() is used for rearranging indexs of list in assending order.
print(l)
l.sort(reverse = True)  # This l.sort() is used for rearranging indexs of list in decending order.
print(l)

# index(). # This method returns the index of the first occurancce of the list item.
print(l.index(2))
print(l)

# count(). # Returns the count of the number of items with the given value.
print(l.count(78))
print(l)

# insert(). # This method insert an item at the given index. User has to specify index and the item to be inserted within the insert() method.
l.insert(1, 500)
print(l)

# extend(). # This method adds an entire list or any other collection datatypes (set,tuple,dictionary.)to the existing list.
m = [100, 200, 300, 400, 500]
l.extend(m)
print(l)

# concatenating two lists: # You can simply concatenate two lists to join two lists.
k = l+m
print(k)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")