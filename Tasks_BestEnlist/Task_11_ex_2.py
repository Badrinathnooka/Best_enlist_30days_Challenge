l1=[1,3,5,7,'d']
l2=[]
for i in range(1,9):
    l2.append(i)
k=tuple(zip(l1,l2))
print(list(k))