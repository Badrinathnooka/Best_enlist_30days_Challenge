l1=[1,2,3,4,5,6,7,8,9,10,12,14]
c=0
for i in l1:
    x=lambda a:(a%2==0)
    y=x(i)
    if(y==True):
        c=c+1
print("The number of even numbers in list are ",c)