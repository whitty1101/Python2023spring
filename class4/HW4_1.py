from tkinter import *
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
root=Tk()
root.title('20230305')
root.geometry('300x300')

def rc(e):
    rval.set('R:'+str(r_scale.get()))

rval=StringVar()
rval.set('r:0')

r_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=rc)
r_scale.grid(row=1,column=0,columnspan=3)

r=Label(root,textvariable=rval)
r.grid(row=0,column=0,columnspan=3,sticky=W)

def gc(e):
    gval.set('G:'+str(g_scale.get()))

gval=StringVar()
gval.set('g:0')

g_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=gc)
g_scale.grid(row=4,column=0,columnspan=3)

g=Label(root,textvariable=gval)
g.grid(row=3,column=0,columnspan=3,sticky=W)

def bc(e):
    bval.set('B:'+str(b_scale.get()))

bval=StringVar()
bval.set('b:0')

b_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=bc)
b_scale.grid(row=6,column=0,columnspan=3)

b=Label(root,textvariable=bval)
b.grid(row=5,column=0,columnspan=3,sticky=W)

root.mainloop()