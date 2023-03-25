print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-------------------------------------------------------------  CONDITIONAL OPERATERS   -------------------------------------------------------------")
# CONDITIONAL OPERATERS = Conditional operators are operators that evaluate a condition and return one of two values based on the result of that evaluation.


# >    :GREATER THAN.
# <    :SMALLER THAN.
# >=   :GREATER THAN OR EQUAL TO.
# <=   :SMALLER THAN OR EQUAL TO.
# ==   :EQUAL TO.
# :=   :NOT EQUAL TO.
a = int(input("Enter your balance: "))
print(a>180)    
print(a<180)    
print(a<=180)   
print(a>=180)   
print(a==180)   
print("-----------------------------------------------------------------  IF, ELSE   ----------------------------------------------------------------------")

a = int(input("Enter your age: ")) 
print("your age is:", a)
if(a>18):
    print("yes")
    print("you can drive your motorcycle or car.")
else:
    print("no")
    print("you can not drive your motorcycle or car.")

appleprice = 500
budget = int(input("Enter your today's budget for shopping: "))
if(appleprice<budget):
    print("murli add the apples in cart.")   
else:
    print("murli do not add the apples in cart.")
 

appleprice = 80     
budget = int(input("Enter your budget: "))      
if(budget-appleprice>50):
    print("murli add 1 kg  apples in cart.")   
else:
    print("murli do not add the apples in cart.")

print("-----------------------------------------------------------------   ELSE   ---------------------------------------------------------------------------")

num = int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative.")
elif(num==0):
    print("Number is zero.")
elif(num==999):
    print("Number is special.")
else:
    print("Number is positive.")

print("I am happy now.")

print("------------------------------------------------------------   NESTED IF STATEMENT   -----------------------------------------------------------------")

num = 18
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10.")
    elif(num>10 and num<=20):
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20.")
else:
    print("Number is zero.")
