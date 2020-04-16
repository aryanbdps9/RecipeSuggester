from tkinter import *
from tkinter.tix import *
import tkinter.ttk as ttk
import random
import time
import recipe_suggester as rs
from functools import partial

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


item=StringVar()




lb1=Label(f1,bg="snow",font=('aria',16,'bold'),text="list of Ingredient",fg="steel blue",bd=10,anchor='w')
lb1.grid(row=0,column=0)

scrollbar = Scrollbar(f1,orient="vertical")
# e3 =tk.Entry(xscrollcommand=scrollbar.set)
# e3.focus()
# e3.pack(side="bottom",fill="y")
#e3.grid(row=10, column=7)

txt1=Entry(f1,xscrollcommand=scrollbar.set,bg="snow",font=('ariel' ,12), textvariable=item , bd=6,insertwidth=4 ,justify='left')
#scrollbar.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=txt1.xview)
txt1.configure(width=100)
txt1.grid(row=0,column=1)

# def format_sep_ing(sep_ingredients):
# 	res = ""


#-------------Button--------------------#
def display(recipe):
    roo=Tk()
    roo.title(recipe['title'])
    roo.configure(bg='snow')
    frame_ = Frame(master=roo)
    frame_.pack(fill=BOTH, expand=True)
    tree = ttk.Treeview(frame_)

    tree['columns'] = ['Quantity']
    tree.column('#0', minwidth=100)
    tree.column('Quantity', minwidth=50)
    tree.heading('#0', text='Ingredient', anchor=W)
    tree.heading('Quantity', text='Quantity', anchor=W)

    for quantity, ingredient in recipe['sep_ingredients']:
        tree.insert("", "end", text=ingredient, values=(quantity,))

    tree.pack(fill=BOTH, expand=True)
    roo.mainloop()


def add_label(root,row_no,col_no,title):
    lb=Label(root,bg="snow",font=('aria',10,),text=title,fg="steel blue",bd=10,anchor='w')
    lb.grid(row=row_no,column=col_no)

def add_button(root,row_no,col_no,title,receipe):
    btn=Button(root,padx=1,pady=1, bd=10 ,fg="black",font=('ariel' ,10),width=10, text=title, bg="powder blue",command=partial(display,receipe))
    btn.grid(row=row_no,column=col_no)


def Ref():
    s=item.get()
    titles,receipes=rs.give_dish(s)
    roo=Tk()
    roo.title("Receipe List")
    # roo.geometry("700x500")
    roo.configure(bg='snow')
    frame_ = Frame(master=roo)
    frame_.pack(fill=BOTH, expand=True)
    swin = ScrolledWindow(frame_, width=700, height=500)
    swin.pack(fill=BOTH, expand=True)
    win = swin.window

    # listbox=Listbox(roo)
    
    #t.insert(END,"ID"+'\t'+"Dish Name")
    s=""
    for i in range(len(titles)):
        add_label(win,i+1,0,titles[i].split('\t')[1])
        add_button(win,i+1,2,"Receipe",receipes[i])
        # add_label(win,i+1,4,receipes[i])
        #t.insert(END,receipes[i]+'\n')
    #t.pack()
    roo.mainloop()



def reset():
    item.set("")
    

btnsearch=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Search", bg="powder blue",command=Ref)
btnsearch.grid(row=6,column=1)
btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Reset", bg="powder blue",command=reset)
btnreset.grid(row=8,column=1)

root.mainloop() # calls the endless loop of the window, so the window will wait for any user interaction till we close it.


