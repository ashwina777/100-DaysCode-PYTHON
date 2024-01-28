# single line comment  use for multiple single lines comment'ctrl + /'
"""
multi line comment or ''' multi comm '''
1.
2. ...
"""
#print("I am a good girl/boy -> error
#      and I love to code") -> wrong way of new line in print statement
print("I am a good girl/boy \n and I love to code")
print("I said \" I love to code \"")
print("Hey",3,4,sep="~")
# default sep is space ' '
# default end is \n new line
#print("Hey",3,4,sep=5,end=3) -> sep and end can't be int (only str)
print("Hey",3,4,sep="~",end="---")
print("Hey",3,4,sep="3",end="---\n")
print("Hey",3,4,sep="3",end="--4")
