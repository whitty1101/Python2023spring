from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk

def add(numlabel,pricelabel):
    numlabel['text']=int(numlabel['text'])+1
    price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
    total=int(totalval.get().split(':')[1].replace('元','').strip())
    totalval.set('共消費:'+str(total+price)+'元')
def minus(numlabel,pricelabel):
    if int(numlabel['text'])>0:
        numlabel['text']=int(numlabel['text'])-1
        price=int(pricelabel['text'].split('.')[1].replace(',','').strip())
        total=int(totalval.get().split(':')[1].replace('元','').strip())
        totalval.set('共消費:'+str(total-price)+'元')
    else:
        messagebox.showwarning('showwarning','The number of product can\'t be below 0')
def sell():
    ana=messagebox.askyesno('Are you sure to pay up?','are you sure to pay up')
    if ana=='yes':
        messagebox.showinfo('')
def showdetail():
    detailWindow =Toplevel(root)
    detailWindow.geometry('850x250')
    table=ttk.Treeview(detailWindow,columns=['Unit Price','Quantity','SUbtotal'])
    table.heading('#0',text='Product Name')
    table.heading('#1',text='Unit Price')
    table.heading('#2',text='Quanity')
    table.heading('#3',text='Subtotal')
    table.column('#0', width=250,anchor=CENTER)
    table.column('#1',anchor=CENTER)
    table.column('#2',anchor=CENTER)
    table.column('#3', anchor=CENTER)
    table.tag_configure('totalcolor',background='#E7E2E2')
    subtotal1=int(p1numlabel['text'])*int(sofa1priceLabel['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=sofa1namelabel['text'],values=[sofa1priceLabel['text'],p1numlabel['text'],subtotal1])
    subtotal2=int(p2numlabel['text'])*int(sofa2priceLabel['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=sofa2namelabel['text'],values=[sofa2priceLabel['text'],p2numlabel['text'],subtotal2])
    subtotal3=int(p3numlabel['text'])*int(sofa3priceLabel['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=sofa3namelabel['text'],values=[sofa3priceLabel['text'],p3numlabel['text'],subtotal3])
    subtotal4=int(p1numlabel['text'])*int(sofa4priceLabel['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=sofa4namelabel['text'],values=[sofa4priceLabel['text'],p4numlabel['text'],subtotal4])
    total=subtotal1+subtotal2+subtotal3+subtotal4
    table.insert('',index='end',text='Total',values=['','',total],tag=('totalcolor'))
    table.pack()
    detailWindow.mainloop()
    


root=Tk()
root.title('KubeTech Shop')
root.geometry('880x650')

titleimg=Image.open("C:/Users/Harrison/Documents/Python_2022Autumn/class10/傳說對決台灣LOGO.png")
titleimg=titleimg.resize((80,40))
titleimg=ImageTk.PhotoImage(titleimg)
titlelabel=Label(root,image=titleimg,width=80,height=40)
titlelabel.grid(row=0,column=0,sticky=W)

sofabutton=Button(root,text='沙發',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2)
sofabutton.grid(row=0,column=1,sticky=W+E)
restbutton=Button(root,text='寢具',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2)
restbutton.grid(row=0,column=2,sticky=W+E)
foodbutton=Button(root,text='廚具',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2)
foodbutton.grid(row=0,column=3,sticky=W+E)
loginbutton=Button(root,text='會員登入/註冊',font=('Inter',18),fg='#1E1E1E',bg='#F8DCDC',width=12,pady=2)
loginbutton.grid(row=0,column=7,sticky=E,padx=5)

banner=Image.open("C:/Users/Harrison/Documents/Python_2022Autumn/class10/maxresdefault.jpg")
banner=banner.resize((852,298))
banner=ImageTk.PhotoImage(banner)
bannerLabel=Label(root,image=banner,width=852,height=298)
bannerLabel.grid(row=1,column=0,columnspan=8,padx=5)

pic1=Image.open("C:/Users/Harrison/Documents/Python_2022Autumn/class10/unnamed.png")
pic1=pic1.resize((202,200))
pic1=ImageTk.PhotoImage(pic1)
pic1Label=Label(root,image=pic1,width=202,height=200)
pic1Label.grid(row=2,column=0,columnspan=2,sticky=W,padx=5)
pic2=Image.open("C:/Users/Harrison/Documents/Python_2022Autumn/class10/unnamed (1).png")
pic2=pic2.resize((202,200))
pic2=ImageTk.PhotoImage(pic2)
pic2Label=Label(root,image=pic2,width=202,height=200)
pic2Label.grid(row=2,column=2,columnspan=2,sticky=W,padx=5)
pic3=Image.open("C:/Users/Harrison/Documents/Python_2022Autumn/class10/unnamed (3).png")
pic3=pic3.resize((202,200))
pic3=ImageTk.PhotoImage(pic3)
pic3Label=Label(root,image=pic3,width=202,height=200)
pic3Label.grid(row=2,column=4,columnspan=2,sticky=W,padx=5)
pic4=Image.open("C:/Users/Harrison/Documents/Python_2022Autumn/class10/unnamed (2).png")
pic4=pic4.resize((202,200))
pic4=ImageTk.PhotoImage(pic4)
pic4Label=Label(root,image=pic4,width=202,height=200)
pic4Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

sofa1namelabel=Label(root,text='狐靈巫女',font=('Inter',10),fg='#000000')
sofa1namelabel.grid(row=3,column=0,columnspan=2,sticky=W,padx=5)
sofa2namelabel=Label(root,text='一拳超神',font=('Inter',10),fg='#000000')
sofa2namelabel.grid(row=3,column=2,columnspan=2,sticky=W,padx=5)
sofa3namelabel=Label(root,text='鋼殼行動',font=('Inter',10),fg='#000000')
sofa3namelabel.grid(row=3,column=4,columnspan=2,sticky=W,padx=5)
sofa4namelabel=Label(root,text='疾光',font=('Inter',10),fg='#000000')
sofa4namelabel.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

sofa1priceLabel=Label(root,text='NT.1,200',font=('Inter',10),fg='#000000')
sofa1priceLabel.grid(row=4,column=0,sticky=W,padx=5)
sofa2priceLabel=Label(root,text='NT.1,200',font=('Inter',10),fg='#000000')
sofa2priceLabel.grid(row=4,column=2,sticky=W,padx=5)
sofa3priceLabel=Label(root,text='NT.1,200',font=('Inter',10),fg='#000000')
sofa3priceLabel.grid(row=4,column=4,sticky=W,padx=5)
sofa4priceLabel=Label(root,text='NT.1,399',font=('Inter',10),fg='#000000')
sofa4priceLabel.grid(row=4,column=6,sticky=W,padx=5)

p1minusbutton=Button(root,text='-',font=('Inter',12),command=lambda: minus(p1numlabel,sofa1priceLabel))
p1minusbutton.grid(row=4,column=1,sticky=W)
p1numlabel=Label(root,text='0',font=('Inter',12,'bold'),fg='#000000')
p1numlabel.grid(row=4,column=1)
p1addbutton=Button(root,text='+',font=('Inter',12),command=lambda: add(p1numlabel,sofa1priceLabel))
p1addbutton.grid(row=4,column=1,sticky=E)

p2minusbutton=Button(root,text='-',font=('Inter',12),command=lambda: minus(p2numlabel,sofa2priceLabel))
p2minusbutton.grid(row=4,column=3,sticky=W)
p2numlabel=Label(root,text='0',font=('Inter',12,'bold'),fg='#000000')
p2numlabel.grid(row=4,column=3)
p2addbutton=Button(root,text='+',font=('Inter',12),command=lambda: add(p2numlabel,sofa2priceLabel))
p2addbutton.grid(row=4,column=3,sticky=E)

p3minusbutton=Button(root,text='-',font=('Inter',12),command=lambda: minus(p3numlabel,sofa3priceLabel))
p3minusbutton.grid(row=4,column=5,sticky=W)
p3numlabel=Label(root,text='0',font=('Inter',12,'bold'),fg='#000000')
p3numlabel.grid(row=4,column=5)
p3addbutton=Button(root,text='+',font=('Inter',12),command=lambda: add(p3numlabel,sofa3priceLabel))
p3addbutton.grid(row=4,column=5,sticky=E)

p4minusbutton=Button(root,text='-',font=('Inter',12),command=lambda: minus(p4numlabel,sofa4priceLabel))
p4minusbutton.grid(row=4,column=7,sticky=W)
p4numlabel=Label(root,text='0',font=('Inter',12,'bold'),fg='#000000')
p4numlabel.grid(row=4,column=7)
p4addbutton=Button(root,text='+',font=('Inter',12),command=lambda: add(p4numlabel,sofa4priceLabel))
p4addbutton.grid(row=4,column=7,sticky=E)

detaillistbutton=Button(root,text='詳細清單',font=('Inter',18),fg='#1E1E1E',bg='#ECEDE7',command=showdetail)


cartimg=Image.open('C:/Users/Harrison/Documents/Python_2022Autumn/class10/image/Shopping Cart.png')
cartimg=cartimg.resize((30,30))
cartimg=ImageTk.PhotoImage(cartimg)
shoppingcartlabel=Label(root,image=cartimg,width=30,height=30)

totalval=StringVar()
totalval.set('共消費:0元') 
totallabel=Label(root,textvariable=totalval,font=('Inter',10),fg='#000000')
checkoutbutton=Button(root,text='結帳',font=('Inter',18),fg='#1E1E1E',bg='#ECEDE7',command=sell)

root.rowconfigure(5,weight=2)
shoppingcartlabel.grid(row=5,column=5,sticky=E+S)
totallabel.grid(row=5,column=6,columnspan=2,sticky=W+S)
checkoutbutton.grid(row=5,column=7,sticky=E+S)
detaillistbutton.grid(row=5,column=0,sticky=S+W,padx=5,pady=1)

root.mainloop()