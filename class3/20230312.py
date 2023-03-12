# from tkinter import *
# import tkinter.ttk as ttk
# from tkscrolledframe import ScrolledFrame

# root=Tk()
# root.title('20230305')
# root.geometry('300x300')

# sframe1=ScrolledFrame(root,width=300,height=300,bg='Black')
# sframe1.pack()
# sframe1.bind_arrow_keys(root)
# sframe1.bind_scroll_wheel(root)
# inter_frame=sframe1.display_widget(Frame)

# btn1=Button(inter_frame,text='1',height=5)
# btn2=Button(inter_frame,text='2',height=5)
# btn3=Button(inter_frame,text='3',height=5)
# btn4=Button(inter_frame,text='4',height=5)
# btn5=Button(inter_frame,text='5',height=5)
# btn1.grid(row=0)
# btn2.grid(row=1)
# btn3.grid(row=2)
# btn4.grid(row=3)
# btn5.grid(row=4)

# root.mainloop()





# from tkinter import *
# import tkinter.ttk as ttk
# from tkscrolledframe import ScrolledFrame

# root=Tk()
# root.title('20230305')
# root.geometry('300x300')

# def choose_brand():
#     titleVar.set('廠牌:'+str(box.current()+1)+','+box.get())

# titleVar=StringVar()
# titleVar.set('廠牌:')

# titlelabel=Label(root,textvariable=titleVar)
# titlelabel.grid(row=0,column=0,sticky=W)

# box=ttk.Combobox(root,values=['BMW','Mercedes benz','Audi'])
# box.grid(column=0,row=1,sticky=W)

# Choose=Button(text='choose',command=choose_brand)
# Choose.grid(column=0,row=2,sticky=W)

# root.mainloop()




# from tkinter import *
# import tkinter.ttk as ttk
# from tkscrolledframe import ScrolledFrame

# root=Tk()
# root.title('20230305')
# root.geometry('300x300')

# def choose_model():
#     statusBar1['text']=listbox.get(listbox.curselection())

# BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
# listVar=StringVar()
# listVar.set(BMW)

# listbox=Listbox(root,selectmode='extended',listvariable=listVar)
# listbox.grid(row=0,column=0)

# btn=Button(root,text='choose',command=choose_model)
# btn.grid(row=1,column=0)

# statusBar1=Label(root,text='',fg='black',bg='white',anchor=W,relief='sunken',bd=2)
# statusBar1.grid(row=3,column=0)

# root.mainloop()




from tkinter import *
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import filedialog
from PIL import Image, ImageTk

root=Tk()
root.title('20230305')
root.geometry('300x300')

def open():
    filePath=filedialog.askopenfilename(title='選取照片',multiple=False,filetypes=[('All Files','*.*'),('PNG','*.png'),('jpg','*.jpg')])
    img=Image.open(filePath)
    resized_image=img.resize((100,100))
    global tk_img
    tk_img=ImageTk.PhotoImage(resized_image)
    imagelabel['image']=tk_img
button=Button(root,text='FU',command=open)
button.pack()
imagelabel=Label(root)
imagelabel.pack()

root.mainloop()

