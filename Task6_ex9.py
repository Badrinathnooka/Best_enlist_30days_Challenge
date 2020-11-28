import math
a=int(input("enter the degree to know the ratios of trignometric function"))
b=int(input("Enter 1)sin 2)cos 3)tan 4)all"))
if(b==1):
    print("sin(",a,") = ",math.sin(a))
elif(b==2):
    print("cos(",a,") = ",math.cos(a))
elif(b==3):
    print("tan(",a,") = ",math.tan(a))
elif(b==4):
    print("sin(",a,") = ",math.sin(a))
    print("cos(",a,") = ",math.cos(a))
    print("tan(",a,") = ",math.tan(a))
else:
    print("Enter valid input")