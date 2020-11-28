l1=[0,4,-1,8,9,-10,-3,-11]
l2=[]
l3=[]
for i in l1:
    if(i>=0):
        l2.append(i)
    else:
        l3.append(i)
print("The positive elements are ",l2)
print("The negative elements are ",l3)