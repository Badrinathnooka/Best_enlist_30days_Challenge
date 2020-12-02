import re
x=input("Enter a string to know it is in uppercase or not :")
p='^[A-Z]{1,}$'
k=re.search(p,x)
if(k):
    print("matched")
else:
    print("not matched")
#print(bool(re.match('^[A-Z]+$','ABC')))