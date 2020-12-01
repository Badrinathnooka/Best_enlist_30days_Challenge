l1=[1,2,3,4,5,6,7,8]
n=int(input("Enter a number to multiply to list :"))
y=list(map(lambda x : (n*x),l1))
print(y)