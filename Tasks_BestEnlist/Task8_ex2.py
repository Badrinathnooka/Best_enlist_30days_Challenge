try:
    a=int(input("Enter a value : "))
    b=int(input("Enter b value : "))
    k=int(input("Enter 1)addition 2)subraction 3)multipication 4)Division"))
    if(k==1):
        print("Addition =",a+b)
    elif(k==2):
        print("Subraction =",a-b)
    elif(k==3):
        print("multiplication =",a*b)
    elif(k==4):
        print("Division = ",a/b)
    else:
        print("Enter a valid number :")
except ZeroDivisionError :
    print("ZeroDivisionError ,Denominator cant be zero")
except ValueError :
    print("value error")
except TypeError :
    print("Its have a Type Error")
except SyntaxError :
    print("syntaxError")
except MemoryError :
    print("MemoryError")
except RuntimeError :
    print("RuntimeError")
except IndentationError :
    print("indentationError")
except Exception as e :
     print("Error",e)
finally :
    print("Thank you")
        