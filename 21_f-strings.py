print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    START    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("-------------------------------------------------------------   STRING FORMATTING   ---------------------------------------------------------------------")
# STRING FORMATING = The string formatting is used for adding variables in string.

letter = ("My name is {}and I am from {}")  
country =("india.")
name =("amanGupta ")
print(letter.format(name, country))  # This is the method of adding variables in string.

letter = ("My name is {1}and I am from {0}")  
country =("india.")
name =("amanGupta ")
print(letter.format(country, name))   # Variables added in leaved curly brakets of string letter.

txt = "This shirt and pant is under: {price:.2f} rupees"
print(txt.format(price = 5999.0999999))

print("------------------------------------------------------------------  F-STRING   ---------------------------------------------------------------------")
# F-STRING = The f-string is the short cut method of string formating.

print(f"My name is {name}and I am from {country}")  # The string formating is defficult than f-string.

price = 5999.0999999
txt = f"This shirt and pant is under: {price:.2f} rupees"
print(txt)

print(f"My name is {name}and I am from {country}") # If you want to show your curly brakets in output then you add two curly barekts like as: {{name}}, {{country}}. most use full for programers.

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    END    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")