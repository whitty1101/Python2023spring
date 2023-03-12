
# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import tkinter.ttk as ttk

# #更改BUTTON內容  WAY1
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('HW1_1')
# root.geometry('400x400+150+200')
# mystringvar=StringVar()
# mystringvar.set('初始化')
# def clicked():
#     mystringvar.set('進行中')
# def clicked1():
#     mystringvar.set('停止')
# mybutton=Button(root,command=clicked,text='start')
# mybutton.pack(pady=20)
# mybutton1=Button(root,command=clicked1,text='stop')
# mybutton1.pack(pady=20)
# label=Label(root,textvariable=mystringvar)
# label.pack()
# root.mainloop()

# #更改BUTTON內容   WAY2
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400+150+200')
# label=Label(root, text='初始化')
# label.pack()
# def clicked():
#     label['text']='進行中'
# def clicked1():
#     label['text']='停止'
# mybutton=Button(root,text='start',command=clicked)
# mybutton.pack(pady=20)
# mybutton1=Button(root,text='stop',command=clicked1)
# mybutton1.pack(pady=20)

# root.mainloop()