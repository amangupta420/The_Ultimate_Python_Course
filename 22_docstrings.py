print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("----------------------------------------------------------------   DOCSTRING   ---------------------------------------------------------------------")
# DOCSTRING = python docstring are the string litrals that appear right after the defination of a function, method, class, or module.

def square(n):
    ''' takes in a number n, returns the square of n '''
    print(n**2)
square(5)
print(square.__doc__)  
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")