print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("----------------------------------------------------------------  WHILE LOOP  ----------------------------------------------------------------------")
# WHILE LOOP =  while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.
i = 0 
# while(i<=3):
#     print(i)
#     i = i+1
# i = int(input("Enter your number: "))
# while(i<=100):
#     i = int(input("Enter your number: "))
#     print(i)

# print("Done with loop")

i = int(input("Enter your number: "))
while(i<=100):
    i = int(input("Enter your number: "))
    print(i)
    i = i+1
    
count = 5                
while(count>0):              
    print(count)         
    count = count - 1     

print("------------------------------------------------------------  ELSE WITH THE WHILE LOOP  ----------------------------------------------------------------------")

count = -5                
while(count>0):             
    print(count)         
    count = count - 1
else:
    print("I am inside else.")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    