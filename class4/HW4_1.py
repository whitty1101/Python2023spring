from tkinter import *
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
#導入
root=Tk()
root.title('20230305')
root.geometry('300x300')
#建議視窗

title1label=Label(root,text='選擇顏色(R,G,B)')
title1label.grid(row=0,column=0,columnspan=2,sticky=W)

#建立SCALE元件
r_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=getValue)
r_scale.grid(row=1,column=0,columnspan=3)

g_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=getValue)
g_scale.grid(row=4,column=0,columnspan=3)

b_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=getValue)
b_scale.grid(row=6,column=0,columnspan=3)

#建立邊提LABEL
title1label1=Label(root,text='r:0')
title1label1.grid(row=1,column=0,columnspan=2,sticky=W)

title1label2=Label(root,text='g:0')
title1label2.grid(row=2,column=0,columnspan=2,sticky=W)

title1label3=Label(root,text='b:0')
title1label3.grid(row=3,column=0,columnspan=2,sticky=W)

#建立LABEL
statusbar=Label(root,text='',fg='white',bg='white')

















def rc(e):
    rval.set('R:'+str(r_scale.get()))
#初始化變數
rval=StringVar()
rval.set('r:0')
#建立變數

r_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=rc)
r_scale.grid(row=1,column=0,columnspan=3)


rl=Label(root,textvariable=rval)
rl.grid(row=0,column=0,columnspan=3,sticky=W)

def gc(e):
    gval.set('G:'+str(g_scale.get()))

gval=StringVar()
gval.set('g:0')

g_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=gc)
g_scale.grid(row=4,column=0,columnspan=3)

gl=Label(root,textvariable=gval)
gl.grid(row=3,column=0,columnspan=3,sticky=W)

def bc(e):
    bval.set('B:'+str(b_scale.get()))

bval=StringVar()
bval.set('b:0')

b_scale= Scale(root,from_=0,to=255,orient=HORIZONTAL,resolution=1,length=300,showvalue=True,command=bc)
b_scale.grid(row=6,column=0,columnspan=3)

bl=Label(root,textvariable=bval)
bl.grid(row=5,column=0,columnspan=3,sticky=W)

#建立getvalue function
def getValue(a):
    #取得RGB
    r=int(r_scale.get())
    g=int(g_scale.get())
    b=int(b_scale.get())
    #16進位
    hex='#{:02x}{:02x}{:02x}'.format(r,g,b)
    #設定STATUSBAR
    =hex
    statusbar['text']=hex
statusbar=Label(root,textvariable=hex,bg='white',relief='sunken')
statusbar.grid(row=7,column=0,sticky=W+E)


root.mainloop()