from tkinter import *

root=Tk()

l1=Label(root,text="Title")
l1.grid(row=0,column=0)

l2=Label(root,text="Author")
l2.grid(row=0,column=2)

l3=Label(root,text="Year")
l3.grid(row=1,column=0)

l4=Label(root,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(root,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(root,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(root,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(root,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(root,height=6,width=35)
list1.grid(row=1,column=0,rowspan=6,columnspan=2)

b1=Button(root,text="VIEW",width=12)
b1.grid(row=2,column=3)

b2=Button(root,text="SEARCH",width=12)
b2.grid(row=3,column=3)

b3=Button(root,text="ADD",width=12)
b3.grid(row=4,column=3)

b4=Button(root,text="UPDATE",width=12)
b4.grid(row=5,column=3)

b5=Button(root,text="DELETE",width=12)
b5.grid(row=6,column=3)

b6=Button(root,text="CLOSE",width=12)
b6.grid(row=7,column=3)

sb1=Scrollbar(root)
sb1.grid(row=3,column=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)






root.mainloop()
