print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("----------------------------------------------------------------   MATCH CASE  ----------------------------------------------------------------------")

x = int(input("Enter the value of x: ")) 
# x is a variable to match.
match x:
    #   If x is 0.
    case 0:
        print("case is zero")
    # Case with if- condition.    
    case 5 if x!=5:
        print("case is not 5")
    #  Empty case with if-condition.
    case _ if 50!=x:
        print(x, "is not 50")
    case _ if 90!=x:
        print(x, "is not 90")
    # default case only be matched.
    # If the above cases were not matched.
    # So it is basically an else method.
    case _:
        print(x)
    
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")