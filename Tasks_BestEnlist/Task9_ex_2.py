from functools import reduce
n=int(input("Enter the number of the fibonnaci numbers : "))
f=lambda n : reduce(lambda x,_ : x+[x[-1]+x[-2]],range(n-2),[0,1])
print(f(n))