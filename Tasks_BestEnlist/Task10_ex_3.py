import re
x=input("Enter a string or sentence to know whether last element contains number or not :")
k=re.search(r'[0-9]\b',x)
if(k):
    print("matched")
else:
    print("not matched")