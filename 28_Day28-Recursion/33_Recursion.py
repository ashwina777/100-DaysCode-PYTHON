def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
   
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
# working
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

def fibonacci(n):
    '''Give the number of terms of fibonacci series you want to find as Arg in 'n' '''
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Input the number of fibonacci series : "))
for i in range(num):
    print(fibonacci(i))