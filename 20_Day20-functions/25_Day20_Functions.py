num = 5
fact=1
for i in range(1,num+1):
    fact *= i
print("factorial of ",num," is : ",fact)
# function for calculating factorial
def calculateFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact *= i
    print("factorial of ",num," is : ",fact)
calculateFactorial(3) 
calculateFactorial(6)
calculateFactorial(1)
calculateFactorial(2)
# function for even odd
def test(num):
    if (num%2==0):
        print("Number ",num," is an even number...")
    else:
        print("Number ",num," is an odd number...")
test(234)
test(875643)
test(3554)

# function for finding number is palindrome or not
def isPalindrome():
    num=int(input("Enter any number : "))
    n=num
    rev=0
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        print(rev)
        num=num//10  # '//' is used as divide operator
    if(n==rev):
        print("Number entered is palindrome as ",n," = ",rev)
    else:
        print("Number entered is not palindrome as ",n," != ",rev)
isPalindrome()

def isGreater(): # this function will be defined later so we use pass ( no error )
    pass  