#program to convert kg to g,pounds,ounce

from tkinter import  *
root=Tk()
def fun():
    g=float(e1_value.get())*1000
    p=float(e1_value.get())*2.20
    o=float(e1_value.get())*35.2
    t1.insert(END,g)
    t2.insert(END,p)
    t3.insert(END,o)


e1_value=StringVar()
e1=Entry(root,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(root,text="Execute",command=fun)
b1.grid(row=0,column=0)

t1=Text(root,height=1,width=10)
t1.grid(row=1,column=0)
t2=Text(root,height=1,width=10)
t2.grid(row=1,column=1)
t3=Text(root,height=1,width=10)
t3.grid(row=1,column=2)

root.mainloop()
