from tkinter import *
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


def remove():
      t=int(input('enter the no of task'))
      del todo[t]
def asce():
    todo.sort()
    print(todo)
def des():
    reverse.tode.sort()
    print(todo)
root=Tk()
root.title('WerkWerkWerk')
root.geometry('500x600')
t=Label(root,text='Get Sh*t Done List',\
        font='12')
t.grid(row=0,column=0,sticky=E)
root.configure(background='lightgreen')
add=Button(root,text='Add to-Do item',font='12',command=add)
add.grid(row=1,column=0,sticky=W)
adde=Entry(root,font='15')
adde.grid(row=1,column=1,sticky=W)
exit=Button(root,text='exit',\
	         command=root.destroy,font='12')
exit.grid(row=8,column=0,sticky=W)
clear=Button(root,text='Clear all tasks',\
              font='12',command=clear)
clear.grid(row=2,column=0,sticky=W)
remove=Button(root,text='Remove',\
              font='12',command=remove)
remove.grid(row=3,column=0,sticky=W)
asce=Button(root,text='ascending sort',\
            font='12',command=asce)
asce.grid(row=4,column=0,sticky=W)
desort=Button(root,text='Sort(DESC)',command=des)
desort.grid(row=5,column=0,sticky=W)
choser=Button(root,text='Choose Random',\
                        font='12')
choser.grid(row=6,column=0,sticky=W)
no=Button(root,text='Number of Tasks',\
           font='12')
no.grid(row=7,column=0,sticky=W)
lstbox = Listbox(root, height=12, width=40)
lstbox.grid(row=2, column=1, rowspan=10, columnspan=2,sticky=E)

root.mainloop()

