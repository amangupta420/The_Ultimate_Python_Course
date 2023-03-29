print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("--------------------------------------------------------------  BREAK FOR LOOP ---------------------------------------------------------------------")
# BREAK = The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

# for i in range(15):
#     if(i == 10):
#         break
#     print("5 X", i+1, "=", 5 * (i+1) )
# print("Breaking out of the loop.")


print("--------------------------------------------------------------  CONTINUE FOR LOOP  -----------------------------------------------------------------")
# CONTINUE = The continue statement skips the rest of the loop statements and causes the next iteration to occur.

for i in range(15):
    if(i == 10):
        print("skip the itration.")
        continue
    print("5 X", i+1, "=", 5 * (i+1) )

print("-------------------------------------------------------------- BREAK WHILE  ----------------------------------------------------------------------")

i = 0
while True:
    i = i + 1
    print(i)
    if(i%50 == 0):
        break
    
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")