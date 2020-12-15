from tkinter import *
root = Tk()
e= Entry(root,width=50)
e.pack()
class Machine:
    def __init__(self):
       self.water = 1000
       self.milk  = 500
       self.coffee = 760
       self.money = 0
    def menu(self): 
        e1=Label(root,text="    Sno   items           price")
        e1.pack()
        e2=Label(root,text="    1)    espresso         2.5 ")
        e2.pack()
        e3=Label(root,text="    2)    latte            2.6 ")
        e3.pack()
        e4=Label(root,text="    3)    cappuccino       2.7 ")
        e4.pack()
    def report(self):
        e1=Label(root,text="    Sno   items          price")
        e1.pack()
        e2=Label(root,text="    1)    water     " +str(self.water)   )
        e2.pack()
        e3=Label(root,text="    2)    milk      " +str(self.milk)     )
        e3.pack()
        e4=Label(root,text="    3)    coffee     "+str(self.coffee) )
        e4.pack()
        e4=Label(root,text="    3)    money     "+str(self.money) )
        e4.pack()
    def espresso(self):
        if(self.water>=50 and self.milk>=30 and self.coffee>=20):
            l=Label(root,text="Insert coins please")
            l.place(x=150,y=10)
            l1 = Label(root,text="quarters")
            l1.place(x=150,y=45)
            t1 = Entry(root)
            t1.place(x=200,y=50)
            l2 = Label(root,text="dimes")
            l2.place(x=150,y=100)
            t2 = Entry(root)
            t2.place(x=200,y=100)
            l3 = Label(root,text="nickel")
            l3.place(x=150,y=200)
            t3 = Entry(root)
            t3.place(x=200,y=200)
            l4=Label(root,text="pennis")
            l4.place(x=150,y=300)
            t4 = Entry(root)
            t4.place(x=200,y=300)
            l5 = Label(root,text="Take ur change ")
            l5.place(x=30,y=400)
            t5=Entry(root,width=100)
            t5.place(x=150,y=400)
            def add1():
                t5.delete(0,'end')
                num1 = float(t1.get())
                num2 = float(t2.get())
                num3 = float(t3.get())
                num4 = float(t4.get())
                r = (num1*0.25) + (0.1*num2) + (num3*0.05) + (num4*0.01)
                if(r>=2.5):
                    p=r-2.5
                    t5.insert(END,str(p))
                    es1 = Label(root,text="Here is your espresso,Enjoy it sir")
                    es1.pack()
                    self.money = self.money+2.5
                    self.water=self.water-50
                    self.milk=self.milk-30
                    self.coffee=self.coffee-20
                else:
                    p="please insert enough coins"
                    t5.insert(END,str(p))
            myButton1 = Button(root,text="change",command=add1)
            myButton1.place(x=300,y=350)
        else:
            es1 = Label(root,text="no products")
            es1.pack()
            
    def latte(self):
        if(self.water>=50 and self.milk>=30 and self.coffee>=20):
            l=Label(root,text="Insert coins please")
            l.place(x=150,y=10)
            l1 = Label(root,text="quarters")
            l1.place(x=150,y=45)
            t1 = Entry(root)
            t1.place(x=200,y=50)
            l2 = Label(root,text="dimes")
            l2.place(x=150,y=100)
            t2 = Entry(root)
            t2.place(x=200,y=100)
            l3 = Label(root,text="nickel")
            l3.place(x=150,y=200)
            t3 = Entry(root)
            t3.place(x=200,y=200)
            l4=Label(root,text="pennis")
            l4.place(x=150,y=300)
            t4 = Entry(root)
            t4.place(x=200,y=300)
            l5 = Label(root,text="Take ur change ")
            l5.place(x=30,y=400)
            t5=Entry(root,width=100)
            t5.place(x=150,y=400)
            def add1():
                t5.delete(0,'end')
                num1 = float(t1.get())
                num2 = float(t2.get())
                num3 = float(t3.get())
                num4 = float(t4.get())
                r = (num1*0.25) + (0.1*num2) + (num3*0.05) + (num4*0.01)
                if(r>=2.6):
                    p=r-2.6
                    t5.insert(END,str(p))
                    es1 = Label(root,text="Here is your Latte,Enjoy it sir")
                    es1.pack()
                    self.money = self.money+2.6
                    self.water=self.water-50
                    self.milk=self.milk-30
                    self.coffee=self.coffee-20
                else:
                    p="please insert enough coins"
                    t5.insert(END,str(p))
            myButton1 = Button(root,text="change",command=add1)
            myButton1.place(x=300,y=350)
        else:
            es1 = Label(root,text="no sufficient products ")
            es1.pack()
    def cappuccino(self):
        if(self.water>=50 and self.milk>=30 and self.coffee>=20):
            l=Label(root,text="Insert coins please")
            l.place(x=150,y=10)
            l1 = Label(root,text="quarters")
            l1.place(x=150,y=45)
            t1 = Entry(root)
            t1.place(x=200,y=50)
            l2 = Label(root,text="dimes")
            l2.place(x=150,y=100)
            t2 = Entry(root)
            t2.place(x=200,y=100)
            l3 = Label(root,text="nickel")
            l3.place(x=150,y=200)
            t3 = Entry(root)
            t3.place(x=200,y=200)
            l4=Label(root,text="pennis")
            l4.place(x=150,y=300)
            t4 = Entry(root)
            t4.place(x=200,y=300)
            l5 = Label(root,text="Take ur change ")
            l5.place(x=30,y=400)
            t5=Entry(root,width=100)
            t5.place(x=150,y=400)
            def add1():
                t5.delete(0,'end')
                num1 = float(t1.get())
                num2 = float(t2.get())
                num3 = float(t3.get())
                num4 = float(t4.get())
                r = (num1*0.25) + (0.1*num2) + (num3*0.05) + (num4*0.01)
                if(r>=2.5):
                    p=r-2.5
                    t5.insert(END,str(p))
                    es1 = Label(root,text="Here is your cappucinno,Enjoy it sir")
                    es1.pack()
                    self.money = self.money+2.5
                    self.water=self.water-50
                    self.milk=self.milk-30
                    self.coffee=self.coffee-20
                else:
                    p="please insert enough coins"
                    t5.insert(END,str(p))
            myButton1 = Button(root,text="change",command=add1)
            myButton1.place(x=300,y=350)
        else:
            es1 = Label(root,text="no sufficient products")
            es1.pack()
def off():
    root.destroy()
def myClick():
    hello = "Hello " + e.get() +" Here is the menu"
    myLabel = Label(root,text=hello)
    myLabel.pack(pady=10) 
    myButton1 = Button(root,text="espresso-$2.5",command=k.espresso)
    myButton1.pack(pady=10)
    myButton2 = Button(root,text="latte-$2.6",command=k.latte)
    myButton2.pack(pady=10)
    myButton3 = Button(root,text="cappuccino-$2.7",command=k.cappuccino)
    myButton3.pack(pady=10)
    myButton4 = Button(root,text="report",command=k.report)
    myButton4.pack(pady=10)
    myButton5 = Button(root,text="OFF",command=off)
    myButton5.pack(pady=10)

myButton = Button(root,text="Enter ur name and click me",command=myClick)
myButton.pack()
k=Machine()


root.mainloop()
