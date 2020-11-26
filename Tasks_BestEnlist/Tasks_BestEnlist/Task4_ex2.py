t1=(1,"Task4",5,"BestEnlist",6)
l1=[]
for i in range(len(t1)-1,-1,-1):#first type 
    l1.append(t1[i])
t2=tuple(l1)
print(t2)

#for i in range(len(t1)-1,-1,-1):#second type
   # print(t1[i])