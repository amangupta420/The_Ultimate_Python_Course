print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-------------------------------------------------------  JOINING SETS USING UNION METHOD    --------------------------------------------------------")
# JOINING SETS USING UNION METHOD = Union() method means, I cam add the two sets using() union method is called union()

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))

print("-----------------------------------------------------------------    UPDATE    --------------------------------------------------------------------")
# UPDATE = Update method is used for updating the value one set to another set.

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.update(s2)
print(s1,s2)

print("--------------------------------------------------------------    INTERSECTION()    ---------------------------------------------------------------")
# INTERSECTION() = which value is present in every set and find them using the intersection are called intersection.

cities1 = {"prayagraj","soraon","mirzapur","satna ghaat"}
cities2 = {"prayagraj","madhyaPradesh","soraon","bhadohi","mirzapur"}
cities3 = cities1.intersection(cities2)
print(cities3)

print("----------------------------------------------------------    INTERSECTION_UPDATE()    --------------------------------------------------------")
# INTERSECTION_UPDATE() = Intersection_Update() method is used for updating set which value is common in first and second set is called in Intersection_Update().

cities1 = {"prayagraj","soraon","mirzapur","satna ghaat"}
cities2 = {"prayagraj","madhyaPradesh","soraon","bhadohi","mirzapur"}
cities1.intersection_update(cities2)
print(cities1)

print("-----------------------------------------------------------    SYMMETRIC_DIFFRENCE()    --------------------------------------------------------")
# SYMMETRIC_DIFFRENCE() = Symmetric_diffrence is used for finding which value is not common in set1 and set2.And it clear that value which is not common in set1 and set2.

cities1 = {"prayagraj","soraon","mirzapur","satna ghaat"}
cities2 = {"prayagraj","madhyaPradesh","soraon","bhadohi","mirzapur"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

print("-----------------------------------------------------------    SYMMETRIC_DIFFRENCE_UPDATE()    --------------------------------------------------------")

cities1 = {"prayagraj","soraon","mirzapur","satna ghaat"}
cities2 = {"prayagraj","madhyaPradesh","soraon","bhadohi","mirzapur"}
cities1.symmetric_difference(cities2)
print(cities1)

print("-----------------------------------------------------------------   DIFFRENCE()    --------------------------------------------------------------")
# DIFFRENCE() = The diffrence() method is used for printing which value is not common in set1 and set2.
  
cities1 = {"prayagraj","soraon","mirzapur","bhadohi","satna ghaat"}
cities2 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
cities3 = cities2.difference(cities1)
print(cities3)

print("--------------------------------------------------------------   DIFFRENCE_UPDATE()    --------------------------------------------------------------")

cities1 = {"prayagraj","soraon","mirzapur","bhadohi","satna ghaat"}
cities2 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
cities2.difference_update(cities1)
print(cities1)

print("--------------------------------------------------------------   ISDISJOINT()    --------------------------------------------------------------")
# ISDISJOINT() = If any values are not common in set1 and set2 then output is comming true is called isdisjoint() method.

cities1 = {"prayagraj2","madhyaPradesh","soraon","mirzapur2"} # In this sets the value is not common then the output is comming ture.
cities2 = {"prayagraj","andhraPradesh","mirzapur"}
print(cities1.isdisjoint(cities2))

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"} # In this sets the value is common then the output is comming false.
cities2 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
print(cities1.isdisjoint(cities2))

print("--------------------------------------------------------------   ISSUPERSET()    --------------------------------------------------------------")
# ISSUPERSET() = The issusreset() method is used for check the value of sets. If the value of set1 is matched to set2 then output is true, is called issuperset() method.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}  
cities2 = {"prayagraj","madhyaPradesh"}
print(cities1.issuperset(cities2))   # cities1 is the sub set of cities2 and cities2 is superset of cities1.

print("--------------------------------------------------------------   ISSUBSET()    --------------------------------------------------------------")
# ISSUBSET() = this method is used for checking subsets.
print(cities2.issubset(cities1))  # cities1 is the sub set of cities2 and cities2 is superset of cities1.

print("--------------------------------------------------------------   ADD()    --------------------------------------------------------------")
# ADD() = Add method is used for adding another value in set.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
cities1.add("andhraPradesh")
print(cities1)

print("--------------------------------------------------------------   REMOVE()    --------------------------------------------------------------")
# REMOVE() = remove method is used for removing any itm to any set.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
cities1.remove("madhyaPradesh")
print(cities1)

print("--------------------------------------------------------------   DISCARD()    --------------------------------------------------------------")
# DISCARD() = discard method is same as remove method but remove method is raises error but discard method not raises error.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
cities1.discard("andhraPradesh")   # here andhraPradesh not present in set then discsrd method is not raiseing any error.
print(cities1)

print("--------------------------------------------------------------   POP()    --------------------------------------------------------------")
# POP() = This method is used for accessing one value to any set.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
item = cities1.pop()
print(item)

print("--------------------------------------------------------------   DEL()    --------------------------------------------------------------")
# DEL() = you can delete any set using del, is called del.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
del cities1
print("hello world") 

print("--------------------------------------------------------------   CLEAR()    --------------------------------------------------------------")
# clear() = you can delete any set using clear, is called clear.

cities1 = {"prayagraj","madhyaPradesh","soraon","mirzapur"}
cities1.clear()
print("hello world") 

print("--------------------------------------------------------------   CHECK IF ITEM EXISTS()    --------------------------------------------------------------")
cities1 = {"prayagraj","madhyaPradesh","soraon",1,5,6,"mirzapur"}

if "prayagraj" in cities1:
    print("yes")
else:
    print("no")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")