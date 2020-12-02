import re
c=0
x=input("Enter a string of length less than 4 to know wheather it has number and which :")
k=re.finditer(r"^([0-9]{1,3})$",x)
for n in k:
    c=1
    print(n.group())
if(c==0):
    print("No matching numbers or length is large")