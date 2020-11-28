a=int(input("Enter a value "))
op=input("Enter the operator for operation ")
b=int(input("Enter b value: "))
def calculator(op):
    if(op=='+'):
        c=a+b
        print(c)
    elif(op=='-'):
        c=a-b
        print(c)
    elif(op=='*'):
        c=a*b
        print(c)
    elif(op=='/'):
        if(b==0):
            print("zero division error")
        else:
            c=a/b
calculator(op)