l1=[1,3,5,7,9]
def add_item(k):
    l1.append(k)
    print("After adding item the update list is",l1)
def delete_item(d):
    l1.remove(d)
    print("After removing an item the updated list is",l1)
k=int(input("Enter any number to add to List"))
add_item(k)
d=int(input("Enter element to delete "))
delete_item(d)
m=max(l1)
print("The largest number in the list is",m)
s=min(l1)
print("The smallest number in the list is",s)
