print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("----------------------------------------------------------------    RECURSION   ---------------------------------------------------------------------")
# RECURSION = recursion is the procces of defining something in term of itself.

# factorial(7) =  7*6*5*4*3*2*1
# factorial(6) =  6*5*4*3*2*1
# factorial(5) =  5*4*3*2*1
# factorial(4) =  4*3*2*1
# factorial(3) =  3*2*1
# factorial(2) =  2*1
# factorial(n) = n*factorial(n-1)

# proccess of def for factorial.
def factorial(n):       # Creating a factorial def and his name puting factorial(n). 
    if(n==0 or n==1):   # If factorial(n) = 0 then he returns in output 1 and if factorial(n) = 1 then he returns in output 1.
        return 1    
    else:               # If factorial(n) is greater than 1 then interpreter follows else method.and this else metod shows in proccess of factorial().in down.
        return n*factorial(n-1)

# proccess of factorial()
"""
suppose that factorial(n) is greater than 1 and his value is 5 then python interpreter returns
 5 * factorial(5-1) now according to python interpreter he says your value is greater than 1
then he leave the if and he will check else than python interpreter repeat this method
again and again. When python interpreter finds 1 which follows if method then python
interpreter check again then if method returns 1.
and its example is given below.
"""
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)

print("----------------------------------------------------------------    QUICK QUIZ   ---------------------------------------------------------------------")

# Write the program to print febbonacci series.
  
f0 = (0)
f1 = (1)
f2 = f(1) + f(0)
fn = f(n-1) + f(n-2)














print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")