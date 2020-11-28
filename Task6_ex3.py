a=0
b=1
k=int(input("Enter number to print of fibonnaci sequence: "))
print("Fibonnaci sequence is :")
print(a)
print(b)
def fib(a,b,k):
    if(b<=k):
     sum1=0
     sum1=a+b
     print(sum1)
     fib(b,sum1,k)
    else:
        return 0
fib(a,b,k)
