import re
x=input("Enter the string :")
if(re.match('^[a-zA-Z0-9]{1,30}$',x)):
    print("Matched")
else:
    print("Not Matched")