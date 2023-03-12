from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk


root=Tk()
root.title('午餐選單')
root.geometry('300x300')

def show():
    text=(checkbtnVal1.get())+''+(checkbtnVal2.get())+''+(checkbtnVal3.get())+''+(checkbtnVal4.get())+''+(checkbtnVal5.get())+''+(checkbtnVal6.get())
    statusBar2['text']=text

checkbtnVal1=StringVar()
checkbtnVal2=StringVar()
checkbtnVal3=StringVar()
checkbtnVal6=StringVar()
checkbtnVal4=StringVar()
checkbtnVal5=StringVar()

title2label=Label(root,text='主餐')
title2label.grid(row=0,column=0,sticky=W)

checkbtn1=Checkbutton(root,text='和牛',variable=checkbtnVal1,onvalue='和牛',offvalue='', fg='Black',command=show)
checkbtn1.grid(row=1, column=0,sticky=W)
checkbtn2=Checkbutton(root,text='伊比利豬',variable=checkbtnVal2,onvalue='伊比利豬',offvalue='', fg='Black',command=show)
checkbtn2.grid(row=1, column=1,sticky=W)
checkbtn3=Checkbutton(root,text='海鮮',variable=checkbtnVal3,onvalue='海鮮',offvalue='', fg='Black',command=show)
checkbtn3.grid(row=1, column=2,sticky=W)
label1=Label(root, text='請選擇飲料')
label1.grid(row=2,column=0,sticky=W)
checkbtn4=Checkbutton(root,text='莊園咖啡',variable=checkbtnVal4,onvalue='莊園咖啡',offvalue='', fg='Black',command=show)
checkbtn4.grid(row=3, column=0,sticky=W)
checkbtn5=Checkbutton(root,text='日月潭紅茶',variable=checkbtnVal5,onvalue='日月潭紅茶',offvalue='', fg='Black',command=show)
checkbtn5.grid(row=3, column=1,sticky=W)
checkbtn6=Checkbutton(root,text='伯爵奶茶',variable=checkbtnVal6,onvalue='伯爵奶茶',offvalue='', fg='Black',command=show)
checkbtn6.grid(row=3, column=2,sticky=W)

statusBar2=Label(root,text='', fg='Black',bg='white',anchor=W, relief="sunken",bd=2)
statusBar2.grid(row=10, column=0, columnspan=6, sticky=W+E+S)

root.mainloop()