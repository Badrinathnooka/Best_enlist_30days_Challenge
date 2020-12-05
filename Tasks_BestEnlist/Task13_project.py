class Machine :
    def __init__(self):
       self.water = 100
       self.milk  = 50
       self.coffee = 76
       self.money = 0
    def menu(self):
        print("Sno   items           price")
        print("1)    espresso         2.5 ")
        print("2)    latte            2.6 ")
        print("3)    cappuccino       2.7 ")
    def items(self,item,name):
        if(item=="espresso"):
            if(self.water>=50 and self.milk>=30 and self.coffee>=20):
                 quarters = float(input("insert quarters :"))
                 dimes    = float(input("insert dimes : "))
                 nickel   = float(input("insert nickel :"))
                 pennies  = float(input("insert pennies :"))
                 total = (quarters*0.25) + (0.1*dimes) + (nickel*0.05) + (pennies*0.01)  
                 cost_espresso = 2.5
                 if(total==cost_espresso):
                     self.money = self.money+cost_espresso
                     self.water=self.water-50
                     self.milk=self.milk-30
                     self.coffee=self.coffee-20
                     print(name,", here is ur",item)
                 elif(total>cost_espresso):
                     change=total-cost_espresso
                     print(f"Here is $",round(change,2),"dollars in change.")
                     self.money = self.money+cost_espresso
                     self.water=self.water-50
                     self.milk=self.milk-30
                     self.coffee=self.coffee-20
                     print(name,", here is ur ",item,"Enjoy.")
                 else:
                     print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry, there is not enough of resources for espresso. ")
        elif(item=="latte"):
            if(self.water>=30 and self.milk>=20 and self.coffee>=10):
                 quarters = float(input("insert quarters :"))
                 dimes    = float(input("insert dimes : "))
                 nickel   = float(input("insert nickel :"))
                 pennies  = float(input("insert pennies :"))
                 total = (quarters*0.25) + (0.1*dimes) + (nickel*0.05) + (pennies*0.01) 
                 cost_latte = 2.6
                 if(total==cost_latte):
                     self.money = self.money+cost_latte
                     self.water=self.water-30
                     self.milk=self.milk-20
                     self.coffee=self.coffee-10
                     print(name,", here is ur",item)
                 elif(total>cost_latte):
                     change=total-cost_latte
                     print(f"Here is $",round(change,2),"dollars in change.")
                     self.money = self.money+cost_latte
                     self.water=self.water-30
                     self.milk=self.milk-20
                     self.coffee=self.coffee-10
                     print(name,", here is ur",item,"Enjoy!")
                 else:
                     print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry, there is not enough of resources for latte ")
        elif(item=="cappuccino"):
            if(self.water>=40 and self.milk>=40 and self.coffee>=15):
                 quarters = float(input("insert quarters :"))
                 dimes    = float(input("insert dimes : "))
                 nickel   = float(input("insert nickel :"))
                 pennies  = float(input("insert pennies :"))
                 total = (quarters*0.25) + (0.1*dimes) + (nickel*0.05) + (pennies*0.01) 
                 cost_cappuccino = 2.7
                 if(total==cost_cappuccino):
                      self.money = self.money+cost_cappuccino
                      self.water=self.water-40
                      self.milk=self.milk-40
                      self.coffee=self.coffee-15
                      print(name,", here is ur",item,"Enjoy!")
                 elif(total>cost_cappuccino):
                     change=total-cost_cappuccino
                     print(f"Here is $",round(change,2),"dollars in change.")
                     self.money = self.money+cost_cappuccino
                     self.water=self.water-40
                     self.milk=self.milk-40
                     self.coffee=self.coffee-15
                     print(name,", here is ur",item,"Enjoy!")
                 else:
                     print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry, there is not enough of resources for cappuccino ")
    def report(self):
        print("water  : ",self.water,"ml")
        print("milk   : ",self.milk,"ml")
        print("coffee : ",self.coffee,"g")
        print("Money  : ","$",self.money)
def customer(p):
 while(p!="off"):
    name=input("Enter ur name please :")
    print("Here is the Menu Sir.What would you like ?")
    k=Machine()
    k.menu()
    op=input("Enter 1)espresso 2)latte 3)cappuccino ")
    if(op=="1" or op=="espresso"):
        k.items("espresso",name)
    elif(op=="2" or op=="latte"):
        k.items("latte",name)
    elif(op=="3" or op=="cappuccino"):
        k.items("cappuccino",name)
    else:
        print("Sorry sir, we dont have that kind of drinks .Please Enter a valid drink as shown in our menu")
        customer(p)
    r=int(input("Enter 1 to view the report :"))
    if(r==1):
        k.report()
    p=input("Enter 'off' to turn off machine or any other key to continue :")
p="on"
customer(p)