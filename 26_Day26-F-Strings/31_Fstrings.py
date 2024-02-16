# f-strings is a new string fomatting (python 3.6 onwards) mechanism
string="Hello my name is {} and i am from {}"
country="India"
name="Ashwina Rawat"
print(string.format(name,country))
string="Hello my name is {1} and i am from {0} "
country="India"
name="Ashwina Rawat"
print(string.format(country,name)) 

print(f"{{name}}Hello my name is {name} and i am from {country}")
# usee {{name}} to simple print {name} while using f-string
#one of the use of f-string

txt="for only {price:.2f} ruppees!"
print(txt.format(price=45.10234))

price = 344.54245
txt=f"for only {price:.2f} ruppees!"
print(txt)
print(txt.format(price=45.10234)) # price will remain 344.54