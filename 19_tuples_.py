print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("------------------------------------------------------------------   TUPLES   ---------------------------------------------------------------------")
# TUPLES = A tuple is a python sequence which stores a group of elements or items. Tuple is same as list but maine diffrence is tuple is immutable.

tuple1 = (1, 2, 3, 4, 5,)   # This is like as list but this is tuple. In tuple coma is compulsory because without coma interpreter not able to excute. tis is tuple.
tuple2 = ("aman", "murli")
print(type(tuple1))
print(type(tuple2))
print(tuple1)
print(tuple2)

print("------------------------------------------------------------    ACCESSING TUPLE ITEMS   ---------------------------------------------------------------------")
# Printing the indexes of tuple1.
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[-4])

print("--------------------------------------------------------------     CHECK FOR ITEMS   ---------------------------------------------------------------------")
# Checking 10 is present in tuple1 or not use to if else method.
if 10 in tuple1:
    print("Yes 10 is present in tuple1.")
else:
    print("No 10 is not present in tuple1.")

print("-----------------------------------------------------------------   RANGE OF INDEX   ---------------------------------------------------------------------")
# You can print a range of tuple items by specifying where do you want to strat, where do you want to end if you want to skip element between the range.

tup = tuple1[1:4]
print(tup)
"""
                                                                        -:IMPORTANT NOTICE:-                                                                        

            Tuple is same as list method only diffrence of mutable and immutable.tuple is immutable and list is mutable and all is sam to same.

"""
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")