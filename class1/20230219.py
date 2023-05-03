from tkinter import *
#引入PILLOW MODULE
from PIL import Image, ImageTk

root=Tk()
root.title('20230219')
root.geometry('1000x500+500+150')
#開啟圖片
img=Image.open('C:/Users/Harrison/Documents/Python2023spring/class1/logo_tree.png')
#轉換為tk圖片物件
tk_img=ImageTk.PhotoImage(img)
#設記程式ICON
root.iconphoto(True,tk_img)

#創立LABEL
label1=Label(root, text='flat',relief='flat')
#建立視窗
label1.pack()
label2=Label(root, text='flat',relief='groove')
label2.pack()
label3=Label(root, text='flat',relief='raised')
label3.pack()
label4=Label(root, text='flat',relief='ridge')
label4.pack()
label5=Label(root, text='flat',relief='solid')
label5.pack()
label6=Label(root, text='flat',relief='sunken')
label6.pack()
label7=Label(root, text='processing',relief='ridge',anchor=W,bd=2)
label7.pack(side='bottom',fill='x')
root.mainloop()

# # from tkinter import *
# # #引入PILLOW MODULE
# # from PIL import Image, ImageTk

# # root=Tk()
# # root.title('20230219')
# # root.geometry('1000x500+500+150')
# # #開啟圖片
# # img=Image.open('C:/Users/User/Documents/Python2023sping/class1/logo_tree.png')
# # #轉換為tk圖片物件
# # tk_img=ImageTk.PhotoImage(img)
# # #設記程式ICON
# # root.iconphoto(True,tk_img)

# # #建立START FUNCTION
# # def start():
# #     label=Label(root,text='processing',anchor=W)
# #     label.pack(side='bottom',fill='x')
# # def stoped():
# #     label2=Label(root,text='DONE',anchor=W)
# #     label2.pack(side='bottom',fill='x')

# # #創立BUTTON
# # start1=Button(root,text='start',command=start)
# # start1.pack()
# # stop=Button(root,text='stop',command=stoped)
# # stop.pack()

# # root.mainloop()


# from tkinter import *
# #引入PILLOW MODULE
# from PIL import Image, ImageTk
# import tkinter.ttk as ttk

# root=Tk()
# root.title('20230219')
# root.geometry('1000x500+500+150')
# #開啟圖片
# img=Image.open('C:/Users/User/Documents/Python2023sping/class1/logo_tree.png')
# #轉換為tk圖片物件
# tk_img=ImageTk.PhotoImage(img)
# #設記程式ICON
# root.iconphoto(True,tk_img)

# #創立一個TABEL
# table=ttk.Treeview(root,columns=['Product Name','Unit Price','Quantity'])
# #create columns title
# table.heading('#0',text='Product Name')
# table.heading('#1',text='Unit Price')
# table.heading('#2',text='Quantity')
# table.heading('#3',text='Subtotal')
# #樂定COLUMN樣式
# table.column('#0',width=250,anchor=CENTER)
# table.column('#1',anchor=CENTER)
# table.column('#2',anchor=CENTER)
# table.column('#3',anchor=CENTER)
# #建立內容從TOTAL行是用淺藍色底
# table.tag_configure('totalcolor',background='#E7E2E2')
# #輸入ROW
# table.insert('',index='end',text='Sofa',values=('20000','2','40000'))
# table.insert('',index='end',text='Sofa',values=('20000','2','40000'),tags='totalcolor')
# table.pack()

# root.mainloop()


# #建立 計算按鈕次數 label 標籤
# mylabel = Button(root, text = "Hello World")
# mylabel.pack()
# #get mylabel的文字內容
# Label(root, text = mylabel["text"]).pack()
# #執行主程式
# root.mainloop()
# ----------------------------------------------------------------------
# #獲取label文字內容-way2
# #建立StringVar
# mystringvar = StringVar()
# mystringvar.set("Hello World!")
# #建立 計算按鈕次數 label 標籤
# mylabel = Button(root, textvariable = mystringvar)
# mylabel.pack()
# #get mylabel的文字內容
# Label(root, text = mystringvar.get()).pack()
# #執行主程式
# root.mainloop()




#更改BUTTON內容  WAY1
from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('HW1_1')
root.geometry('400x400+150+200')
x=0
def clicked():
    global x
    x=x+1
    mystringvar.set('click'+str(x))
mystringvar=StringVar()
mystringvar.set("click")
mybutton=Button(root,textvariable=mystringvar,command=clicked)
mybutton.pack(pady=20)
root.mainloop()