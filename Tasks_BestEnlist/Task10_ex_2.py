import re
#x='acbd is ab good boy'
x=input("Enter a string")
p='\w*ab.\w*'
k=re.search(p,x)
if(k):
    print(k.group())
    print("matched")
else:
    print("not matched")