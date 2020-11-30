try:
    try :
        l1=[1,3,5,7,9]
        print(l1[6])
    except IndexError :
        print("List Index out of range")
    try :
        print(tupl)
    except NameError :
        print("Name Error,Name is not defined")
    try :
        k=3/0
    except ZeroDivisionError :
        print("Division by Zero is not possible")
    try :
        k=int(input("Enter alphabet for error :"))
    except ValueError :
        print("Value error ")
except RuntimeError :
    print("Runtime Error ")
except TypeError :
    print("Type Error")
except SyntaxError :
    print("somewhere its a syntax error")
except RuntimeError :
    print("Runtime Error")
except ImportError :
    print("import Error")
except Exception as e:
    print("Error is ",e)
finally :
    print("Thank you")