# Match case is new feature in python 3.10 onwards
# It is similar to the switch case used in java,c,'c++.
x=90
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x < 10:
        print("X is < 10") # if previous conditions are met then this will not execute
    case _ if x > 10:
        print("X is > 10")
    case _ if x ==90:
        print(x," is  90") 
    # even if x is 90 but greater than 10 condition is met before and thus this will not execute
    
    case _ if x !=80:         
        print(x," is not 80") # if
    case _:
        print(x)              # else