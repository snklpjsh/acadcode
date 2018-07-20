from tkinter import *
import random
from tkinter import Tk

todo=[]
def clear():
    lstbox.delete(0,"end")
def updateli():
    clear()
    for task in todo:
        lstbox.insert("end",task)
def add():
    x=adde.get()
    if(x!=""):
        todo.append(x)
        updateli()

def clearf():
    lstbox.delete(0,"end")
    todo.clear()

def remove():
    p=lstbox.get("active")
    if p in todo:
        todo.remove(p)
        updateli()
def asce():
    todo.sort()
    updateli()
def des():
    todo.sort(reverse=TRUE)
    updateli()
root=Tk()
def chose():
        z =random.choice(todo)
        l = Label(root, text=z, font='12', width='20', bg="white")
        l.grid(row=11, column=1, sticky=W)
def count():
         c=len(todo)
         l1=Label(root,text=c,font='12',width='20',bg="white")
         l1.grid(row=12,column=1,sticky=W)


root.title('WerkWerkWerk')
root.geometry('500x600')
t=Label(root,text='Get Sh*t Done List',\
        font='12')
t.grid(row=0,column=0,sticky=E)
root.configure(background='lightgreen')
addb=Button(root,text='Add to-Do item',font='12',command=add)
addb.grid(row=1,column=0,sticky=W)
adde=Entry(root,font='15')
adde.grid(row=1,column=1,sticky=W)
exit=Button(root,text='exit',\
	         command=root.destroy,font='12')
exit.grid(row=8,column=0,sticky=W)
clearb=Button(root,text='Clear all tasks',\
              font='12',command=clearf)
clearb.grid(row=2,column=0,sticky=W)
removeb=Button(root,text='Remove',\
              font='12',command=remove)
removeb.grid(row=3,column=0,sticky=W)
asceb=Button(root,text='ascending sort',\
            font='12',command=asce)
asceb.grid(row=4,column=0,sticky=W)
desortb=Button(root,text='Sort(DESC)',command=des)
desortb.grid(row=5,column=0,sticky=W)
choserb=Button(root,text='Choose Random',\
                        font='12',command=chose)
choserb.grid(row=6,column=0,sticky=W)
no=Button(root,text='Number of Tasks',\
           font='12',command=count)
no.grid(row=7,column=0,sticky=W)
lstbox = Listbox(root, height=12, width=40)
lstbox.grid(row=2, column=1, rowspan=10, columnspan=2,sticky=E)

root.mainloop()

