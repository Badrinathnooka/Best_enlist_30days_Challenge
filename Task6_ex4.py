a=int(input("Enter a number:"))
order = len(str(a))
b=a
sum1=0
while(a!=0):
    temp = a%10
    sum1 = sum1 + pow(temp,order)
    a=a//10
if(sum1==b):
    print(b,"is a Armstrong number" )
else:
    print(b,"is not a Armstrong number" )