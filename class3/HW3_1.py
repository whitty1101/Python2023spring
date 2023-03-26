from tkinter import *
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
root=Tk()
root.title('20230305')
root.geometry('300x300')

BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
listVar=StringVar()
listVar.set(BMW)

listbox=Listbox(root,selectmode='extended',listvariable=listVar)
listbox.grid(row=3,column=0)


def choose_brand():
    titleVar.set('廠牌:'+str(box.current()+1)+','+box.get())

titleVar=StringVar()
titleVar.set('廠牌:')

titlelabel=Label(root,textvariable=titleVar)
titlelabel.grid(row=0,column=0,sticky=W)

box=ttk.Combobox(root,values=['BMW','Mercedes benz','Audi'])
box.grid(column=0,row=1,sticky=W)

Choose=Button(text='choose',command=choose_brand)
Choose.grid(column=0,row=2,sticky=W)

root.mainloop()