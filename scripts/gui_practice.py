from tkinter import *
import random
import time
import recipe_suggester as rs

# class App:
#   def __init__(self, root):
#     fm = Frame(root, width=1600, height=700, bg="snow")
#     fm.pack(side=TOP, expand=NO, fill=NONE)
root =Tk()
#display = App(root)
root.title("Food Finder")
root.geometry("1600x700+0+0")
root.configure(bg='snow')
#-------------------------------------------------#
Tops = Frame(root,bg="snow",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

lblinfo = Label(Tops, bg="snow",font=( 'aria,' ,30, 'bold' ),text="Food Finder",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

#----------------------------------------------------#
f1 = Frame(root,bg="snow",width = 1600,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

# f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
# f2.pack(side=RIGHT)


item1=StringVar()
item2=StringVar()
item3=StringVar()
item4=StringVar()
item5=StringVar()
item6=StringVar()
item7=StringVar()
item8=StringVar()



lb1=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 1",fg="steel blue",bd=10,anchor='w')
lb1.grid(row=0,column=0)
txt1=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item1 , bd=6,insertwidth=4 ,justify='right')
txt1.grid(row=0,column=1)

lb2=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 2",fg="steel blue",bd=10,anchor='w')
lb2.grid(row=1,column=0)
txt2=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item2 , bd=6,insertwidth=4 ,justify='right')
txt2.grid(row=1,column=1)

lb3=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 3",fg="steel blue",bd=10,anchor='w')
lb3.grid(row=2,column=0)
txt3=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item3 , bd=6,insertwidth=4 ,justify='right')
txt3.grid(row=2,column=1)

lb4=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 4",fg="steel blue",bd=10,anchor='w')
lb4.grid(row=3,column=0)
txt4=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item4 , bd=6,insertwidth=4,justify='right')
txt4.grid(row=3,column=1)

lb5=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 5",fg="steel blue",bd=10,anchor='w')
lb5.grid(row=0,column=2)
txt5=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item5 , bd=6,insertwidth=4,justify='right')
txt5.grid(row=0,column=3)

lb6=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 6",fg="steel blue",bd=10,anchor='w')
lb6.grid(row=1,column=2)
txt6=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item6 , bd=6,insertwidth=4,justify='right')
txt6.grid(row=1,column=3)

lb7=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 7",fg="steel blue",bd=10,anchor='w')
lb7.grid(row=2,column=2)
txt7=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item7 , bd=6,insertwidth=4,justify='right')
txt7.grid(row=2,column=3)

lb8=Label(f1,bg="snow",font=('aria',16,'bold'),text="Ingredient 8",fg="steel blue",bd=10,anchor='w')
lb8.grid(row=3,column=2)
txt8=Entry(f1,bg="snow",font=('ariel' ,16,'bold'), textvariable=item8 , bd=6,insertwidth=4,justify='right')
txt8.grid(row=3,column=3)


#-------------Button--------------------#


lbl= Label(f1,bg="snow",text="")
lbl.grid(row=6,column=2)
def Ref():
	s=""
	s+=item1.get()
	s+=","
	s+=item2.get()
	s+=","
	s+=item3.get()
	s+=","
	s+=item4.get()
	s+=","
	s+=item5.get()
	s+=","
	s+=item6.get()
	s+=","
	s+=item7.get()
	s+=","
	s+=item8.get()
	s+=","
	l=rs.give_dish(s)



def reset():
	item1.set("")
	item2.set("")
	item3.set("")
	item4.set("")
	item5.set("")
	item6.set("")
	item7.set("")
	item8.set("")

btnsearch=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Search", bg="powder blue",command=Ref)
btnsearch.grid(row=6,column=2)
btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Reset", bg="powder blue",command=reset)
btnreset.grid(row=8,column=2)




























root.mainloop() # calls the endless loop of the window, so the window will wait for any user interaction till we close it.


