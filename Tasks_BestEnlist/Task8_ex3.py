try:
    m=int(input("Enter any value :"))
    print(BestEnlist_python)
except NameError :
    print("NameError, Name is not defined")
except Exception as e:
    print("Error is ",e)
finally :
    print("bye")