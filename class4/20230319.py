# from tkinter import *
# import tkinter.ttk as ttk
# from tkscrolledframe import ScrolledFrame
# root=Tk()
# root.title('20230305')
# root.geometry('300x300')

# year_scale= Scale(root,from_=0,to=100)
# year_scale.grid(row=1,column=0,columnspan=3)

# root.mainloop()





# from tkinter import *
# import tkinter.ttk as ttk
# from tkscrolledframe import ScrolledFrame
# root=Tk()
# root.title('20230305')
# root.geometry('300x300')

# def get(e):
#     value.set('年齡:'+str(year_scale.get()))

# value=StringVar()
# value.set('年齡:0')

# year_scale= Scale(root,from_=0,to=100,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=get)
# year_scale.grid(row=0,column=0,columnspan=3)

# status_bar=Label(root,textvariable=value,)
# status_bar.grid(row=2,column=0,columnspan=3,sticky=W+E+S)

# root.mainloop()



# from tkinter import *
# import tkinter.ttk as ttk
# from tkscrolledframe import ScrolledFrame
# root=Tk()
# root.title('20230305')
# root.geometry('300x300')

# def get(e):
#     value.set('年齡:'+str(height.get()))

# value=StringVar()

# title1label2=Label(root,text='height:')
# title1label2.grid(row=3,column=0,columnspan=2,sticky=W)

# title1label3=Label(root,textvariable=value)
# title1label3.grid(row=3,column=1,columnspan=2,sticky=W)

# height=Spinbox(root,from_=99,to=250, textvariable=value)
# height.grid(row=4,column=0,columnspan=3,sticky=W+E+S)

# root.mainloop()