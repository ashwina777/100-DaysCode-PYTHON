# String functions
a=" aShwinA Raw at!!! !!!! !! !!! !!!!!"
b="heLlo world ! "
print(len(a))
print(a.upper())  # converts str to uppercase
print(a)  # Strings are immutable
print(a.lower())  # converts str to lowercase
print(a.strip())  # removes any white spaces before and after the string
print(a.rstrip("!"),"hey") # removes any (only)trailing char 
print(a.rstrip("R"),"ashwina") # does not work 
print(a.replace("a","E"))
print(a.replace("A","@")) # case sensitive
print(a.split(" ")) # split given str at specified instance and returns separated str as list items
print(a.capitalize()) # capitalise the first alphabet
print(b.capitalize()) # capitalise the first alphabet
print(a.center(40))  # aligns the str to the centre as per parameters given by user
print(b.center(40))  
print(b.center(100))  
print(a.count("!"))  # returns number to times the given value has occured within the given str
print(a.count("!!!"))  # output 4 counts in each consecutive str without space
print(a.count("A"))  # o/p = 1 (case sensitive)
print(a.endswith("!!")) # checks if the str ends with given value
print(a.endswith("R",1,10)) # remember it excludes the last value and is case sensitive
print(a.endswith("Ra",1,10)) 
print(a.endswith("A R",1,10)) 
print(a.startswith("a")) # checks if the str starts with given value
print(a.startswith("a",1,10)) # remember it excludes the last value and is case sensitive
print(a.find("A")) # returns the index of the first occurence of the given value
print(a.find("a",2,10)) # returns -1 if the value is not found excluding the given range-10 (case sensitive)
print(a.index("A")) # returns the index of the first occurence of the given value
# difference between find and index is that find returns -1 if the value is not found whereas index returns an error
#print(a.index("a",2,10)) # returns an error if the value is not found excluding the given range-10 ValueError: substring not found
print(a.isalnum()) # returns true if the str is alphanumeric (no spaces) A-Z,a-z,0-9
print(a.isalpha()) # returns true if the str is alphabetic (no spaces) A-Z,a-z
print(a.islower()) # returns true if the str is in lowercase
print(a.isupper()) # returns true if the str is in uppercase
print(a.isspace()) # returns true if the str is a space
print(a.isprintable()) # returns true if the str is printable (no special characters) eg: \n,\t not printable
print(a.istitle()) # returns true if the str is in title case (first letter of each word is capitalised)
print(a.swapcase()) # swaps the case of the str (lowercase to uppercase and vice versa)
print(a.title()) # converts the str to title case (first letter of each word is capitalised)