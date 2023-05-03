from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import smtplib
from tkinter import *
import tkinter.ttk as ttk
from tkscrolledframe import ScrolledFrame
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Text

home=Tk()
home.title('KubeTech Shop')
home.geometry('1920x1080')
# Create a ScrolledFrame widget
sframe1 = ScrolledFrame(home,width=1920, height=1080,bg='White')
sframe1.grid(row=0,column=0)
sframe1.bind_arrow_keys(home)
sframe1.bind_scroll_wheel(home)
inner_frame = sframe1.display_widget(Frame)

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
        payup=Toplevel()
        payup.geometry('850x850')
def showdetail():
    detailWindow =Toplevel(home)
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
    s1=int(numl1['text'])*int(pl1['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel1['text'],values=[pl1['text'],namel1['text'],s1])
    s2=int(numl2['text'])*int(pl2['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel2['text'],values=[pl2['text'],namel2['text'],s2])
    s3=int(numl3['text'])*int(pl3['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel3['text'],values=[pl3['text'],namel3['text'],s3])
    s4=int(numl4['text'])*int(pl4['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel4['text'],values=[pl4['text'],namel4['text'],s4])
    s5=int(numl5['text'])*int(pl5['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel5['text'],values=[pl5['text'],namel5['text'],s5])
    s6=int(numl6['text'])*int(pl6['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel6['text'],values=[pl6['text'],namel6['text'],s6])
    s7=int(numl7['text'])*int(pl7['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel7['text'],values=[pl7['text'],namel7['text'],s7])
    s8=int(numl8['text'])*int(pl8['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel8['text'],values=[pl8['text'],namel8['text'],s8])
    s9=int(numl9['text'])*int(pl9['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel9['text'],values=[pl9['text'],namel9['text'],s9])
    s10=int(numl10['text'])*int(pl10['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel10['text'],values=[pl10['text'],namel10['text'],s10])
    s11=int(numl11['text'])*int(pl11['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel11['text'],values=[pl11['text'],namel11['text'],s11])
    s12=int(numl12['text'])*int(pl12['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel12['text'],values=[pl12['text'],namel12['text'],s12])
    s13=int(numl13['text'])*int(pl13['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel13['text'],values=[pl13['text'],namel13['text'],s13])
    s14=int(numl14['text'])*int(pl14['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel14['text'],values=[pl14['text'],namel14['text'],s14])
    s15=int(numl15['text'])*int(pl15['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel15['text'],values=[pl15['text'],namel15['text'],s15])
    s16=int(numl16['text'])*int(pl16['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel16['text'],values=[pl16['text'],namel16['text'],s16])
    s17=int(numl17['text'])*int(pl17['text'].split('.')[1].replace(',','').strip())
    table.insert('',index='end',text=namel17['text'],values=[pl17['text'],namel17['text'],s17])

    total=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12+s13+s14+s15+s16+s17
    table.insert('',index='end',text='Total',values=['','',total],tag=('totalcolor'))
    table.grid(row=0,column=0)
    detailWindow.mainloop()
def logWin():
    log=Toplevel(home)
    enterEmail=Label(log,text='Please enter your Email:      ')
    emailEntryBox=ttk.Entry(log)
    emailSent=Button(log, text='enter', command=lambda:email(emailEntryBox))
    enterEmail.grid(row=0,column=0)
    emailEntryBox.grid(row=0,column=1)
    emailSent.grid(row=2,column=2)
def email(emailEntryBox):
    #建立EMAIL物件
    text=MIMEText('You had login in EShop')
    #use bytes
    #建立並設定物件
    content=MIMEMultipart()#建立物件
    content['subject']='Login!!!'#郵件TITLE
    content['from']='bagelcatboy@gmail.com'#寄件者
    content['to']=emailEntryBox.get()#收件者
    print(emailEntryBox.get())
    #郵件內容使用MIMEMULTIPART物件的ATTACHMETHOD進行設定
    content.attach(text)#郵件內容
    #建立SMTPLIB物件
    smtp=smtplib.SMTP(host='smtp.gmail.com',port='587')
    #利用WITH來釋放資源
    with open('project/password.txt','r') as f:
        mailToken=f.read()
    with smtp:#利用with來釋放資源
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('bagelcatboy@gmail.com',mailToken)
            smtp.send_message(content)
            print('sent')
            smtp.quit()
        except Exception as e:
            print('Error message:',e)
def foodWin():
    food=Toplevel(home)
    food.geometry('1920x1080')
    homebutton=Button(home,text='tools',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=homeWin)
    homebutton.grid(row=0,column=1,sticky=W+E)
    gamesbutton=Button(home,text='games',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=gameWin)
    gamesbutton.grid(row=0,column=2,sticky=W+E)
    toolsbutton=Button(home,text='tools',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=toolWin)
    toolsbutton.grid(row=0,column=3,sticky=W+E)



def gameWin():
    game=Toplevel(home)
    game.geometry('1920x1080')
    homebutton=Button(home,text='tools',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=homeWin)
    homebutton.grid(row=0,column=1,sticky=W+E)
    foodbutton=Button(home,text='food',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=foodWin)
    foodbutton.grid(row=0,column=2,sticky=W+E)
    toolsbutton=Button(home,text='tools',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=toolWin)
    toolsbutton.grid(row=0,column=3,sticky=W+E)
def toolWin():
    tool=Toplevel(home)
    tool.geometry('1920x1080')
    homebutton=Button(home,text='tools',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=homeWin)
    homebutton.grid(row=0,column=1,sticky=W+E)
    foodbutton=Button(home,text='food',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=foodWin)
    foodbutton.grid(row=0,column=2,sticky=W+E)
    gamesbutton=Button(home,text='games',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=gameWin)
    gamesbutton.grid(row=0,column=3,sticky=W+E)
def homeWin():
    home=Tk()
    home.title('KubeTech Shop')
    home.geometry('1920x1080')

    




titleimg=Image.open("C:/Users/Harrison/Documents/Python2023spring/project/Screenshot 2023-03-26 212121.png")
titleimg=titleimg.resize((80,80))
titleimg=ImageTk.PhotoImage(titleimg)
titlelabel=Label(inner_frame,image=titleimg,width=80,height=40)
titlelabel.grid(row=0,column=0,sticky=W)

foodbutton=Button(inner_frame,text='food',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=foodWin)
foodbutton.grid(row=0,column=1,sticky=W+E)
gamesbutton=Button(inner_frame,text='games',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=gameWin)
gamesbutton.grid(row=0,column=2,sticky=W+E)
toolsbutton=Button(inner_frame,text='tools',font=('Inter',18),fg='#1E1E1E',bg='#ECE8E7',width=5,pady=2,command=toolWin)
toolsbutton.grid(row=0,column=3,sticky=W+E)

loginbutton=Button(inner_frame,text='會員登入/註冊',font=('Inter',18),fg='#1E1E1E',bg='#F8DCDC',width=12,pady=2,command=logWin)
loginbutton.grid(row=0,column=10,sticky=E,padx=5)

banner=Image.open("project/taiwanese-beef-noodle-soup-4777014-hero-01-e06a464badec476684e513cad44612da.jpg")
banner=banner.resize((750,500))
banner=ImageTk.PhotoImage(banner)
bannerLabel=Label(inner_frame,image=banner,width=750,height=500)
bannerLabel.grid(row=1,column=0,columnspan=10,padx=5)

p1=Image.open("project/220428140436-04-classic-american-hamburgers.jpg")
p1=p1.resize((202,200))
p1=ImageTk.PhotoImage(p1)
p1Label=Label(inner_frame,image=p1,width=202,height=200)
p1Label.grid(row=2,column=0,columnspan=2,sticky=W,padx=5)

p2=Image.open("project/Bananas-5c6a36a346e0fb0001f0e4a3.jpg")
p2=p2.resize((202,200))
p2=ImageTk.PhotoImage(p2)
p2Label=Label(inner_frame,image=p2,width=202,height=200)
p2Label.grid(row=2,column=2,columnspan=2,sticky=W,padx=5)

p3=Image.open("project/cherries-royalty-free-image-1656341880.jpg")
p3=p3.resize((202,200))
p3=ImageTk.PhotoImage(p3)
p3Label=Label(inner_frame,image=p3,width=202,height=200)
p3Label.grid(row=2,column=4,columnspan=2,sticky=W,padx=5)

p4=Image.open("project/Fresh-Raw-Salmon_horiz.jpg")
p4=p4.resize((202,200))
p4=ImageTk.PhotoImage(p4)
p4Label=Label(inner_frame,image=p4,width=202,height=200)
p4Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p5=Image.open("project/health-benefits-of-pears-main-image-cd5bb15.jpg")
p5=p5.resize((202,200))
p5=ImageTk.PhotoImage(p5)
p5Label=Label(inner_frame,image=p4,width=202,height=200)
p5Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p6=Image.open("project/mango-fruit-sugar-1530136260.jpg")
p6=p6.resize((202,200))
p6=ImageTk.PhotoImage(p6)
p6Label=Label(inner_frame,image=p4,width=202,height=200)
p6Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p7=Image.open("project/minestrone-soup-recipe-22.jpg")
p7=p7.resize((202,200))
p7=ImageTk.PhotoImage(p7)
p7Label=Label(inner_frame,image=p4,width=202,height=200)
p7Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p8=Image.open("project/p0dx4wkz.jpg")
p8=p8.resize((202,200))
p8=ImageTk.PhotoImage(p8)
p8Label=Label(inner_frame,image=p4,width=202,height=200)
p8Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p9=Image.open("project/pexels-ash-376464.jpg")
p9=p9.resize((202,200))
p9=ImageTk.PhotoImage(p9)
p9Label=Label(inner_frame,image=p4,width=202,height=200)
p9Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p10=Image.open("project/photo-1550258987-190a2d41a8ba.jpg")
p10=p10.resize((202,200))
p10=ImageTk.PhotoImage(p10)
p10Label=Label(inner_frame,image=p4,width=202,height=200)
p10Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p11=Image.open("project/raw-green-organic-golden-pomelo-1078669424.jpg")
p11=p11.resize((202,200))
p11=ImageTk.PhotoImage(p11)
p11Label=Label(inner_frame,image=p4,width=202,height=200)
p11Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p12=Image.open("project/shutterstock_226100671.jpg")
p12=p12.resize((202,200))
p12=ImageTk.PhotoImage(p12)
p12Label=Label(inner_frame,image=p4,width=202,height=200)
p12Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p13=Image.open("project/sous-vide-brisket-mfs-193-4x3-1-24930daf16854a9091eaff1503aac157.jpg")
p13=p13.resize((202,200))
p13=ImageTk.PhotoImage(p13)
p13Label=Label(inner_frame,image=p4,width=202,height=200)
p13Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p14=Image.open("project/taiwanese-beef-noodle-soup-4777014-hero-01-e06a464badec476684e513cad44612da.jpg")
p14=p14.resize((202,200))
p14=ImageTk.PhotoImage(p14)
p14Label=Label(inner_frame,image=p4,width=202,height=200)
p14Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p15=Image.open("project/istockphoto-654971856-612x612.jpg")
p15=p15.resize((202,200))
p15=ImageTk.PhotoImage(p15)
p15Label=Label(inner_frame,image=p15,width=202,height=200)
p15Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p16=Image.open("project/istockphoto-654971856-612x612.jpg")
p16=p16.resize((202,200))
p16=ImageTk.PhotoImage(p16)
p16Label=Label(inner_frame,image=p16,width=202,height=200)
p16Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

p17=Image.open("project/istockphoto-654971856-612x612.jpg")
p17=p17.resize((202,200))
p17=ImageTk.PhotoImage(p17)
p17Label=Label(inner_frame,image=p17,width=202,height=200)
p17Label.grid(row=2,column=6,columnspan=2,sticky=W,padx=5)

namel1=Label(inner_frame,text='hamburger',font=('Inter',10),fg='#000000')
namel1.grid(row=3,column=0,columnspan=2,sticky=W,padx=5)

namel2=Label(inner_frame,text='banna',font=('Inter',10),fg='#000000')
namel2.grid(row=3,column=2,columnspan=2,sticky=W,padx=5)

namel3=Label(inner_frame,text='cheery',font=('Inter',10),fg='#000000')
namel3.grid(row=3,column=4,columnspan=2,sticky=W,padx=5)

namel4=Label(inner_frame,text='raw salmon',font=('Inter',10),fg='#000000')
namel4.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel5=Label(inner_frame,text='pears',font=('Inter',10),fg='#000000')
namel5.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel6=Label(inner_frame,text='mango',font=('Inter',10),fg='#000000')
namel6.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel7=Label(inner_frame,text='soup',font=('Inter',10),fg='#000000')
namel7.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel8=Label(inner_frame,text='strawberry',font=('Inter',10),fg='#000000')
namel8.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel9=Label(inner_frame,text='pan cakes',font=('Inter',10),fg='#000000')
namel9.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel10=Label(inner_frame,text='pineapple',font=('Inter',10),fg='#000000')
namel10.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel11=Label(inner_frame,text='lemon',font=('Inter',10),fg='#000000')
namel11.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel12=Label(inner_frame,text='apple',font=('Inter',10),fg='#000000')
namel12.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel13=Label(inner_frame,text='beef',font=('Inter',10),fg='#000000')
namel13.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel14=Label(inner_frame,text='beef noodles',font=('Inter',10),fg='#000000')
namel14.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel15=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
namel15.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel16=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
namel16.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)

namel17=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
namel17.grid(row=3,column=6,columnspan=2,sticky=W,padx=5)


pl1=Label(inner_frame,text='NT.89',font=('Inter',10),fg='#000000')
pl1.grid(row=4,column=0,sticky=W,padx=5)

pl2=Label(inner_frame,text='NT.40',font=('Inter',10),fg='#000000')
pl2.grid(row=4,column=2,sticky=W,padx=5)

pl3=Label(inner_frame,text='NT.55',font=('Inter',10),fg='#000000')
pl3.grid(row=4,column=4,sticky=W,padx=5)

pl4=Label(inner_frame,text='NT.65',font=('Inter',10),fg='#000000')
pl4.grid(row=4,column=6,sticky=W,padx=5)

pl4=Label(inner_frame,text='NT.60',font=('Inter',10),fg='#000000')
pl4.grid(row=4,column=6,sticky=W,padx=5)

pl5=Label(inner_frame,text='NT.20',font=('Inter',10),fg='#000000')
pl5.grid(row=4,column=6,sticky=W,padx=5)    

pl6=Label(inner_frame,text='NT.50',font=('Inter',10),fg='#000000')
pl6.grid(row=4,column=6,sticky=W,padx=5)

pl7=Label(inner_frame,text='NT.120',font=('Inter',10),fg='#000000')
pl7.grid(row=4,column=6,sticky=W,padx=5)

pl8=Label(inner_frame,text='NT.110',font=('Inter',10),fg='#000000')
pl8.grid(row=4,column=6,sticky=W,padx=5)

pl9=Label(inner_frame,text='NT.115',font=('Inter',10),fg='#000000')
pl9.grid(row=4,column=6,sticky=W,padx=5)

pl10=Label(inner_frame,text='NT.60',font=('Inter',10),fg='#000000')
pl10.grid(row=4,column=6,sticky=W,padx=5)

pl11=Label(inner_frame,text='NT.25',font=('Inter',10),fg='#000000')
pl11.grid(row=4,column=6,sticky=W,padx=5)

pl12=Label(inner_frame,text='NT.30',font=('Inter',10),fg='#000000')
pl12.grid(row=4,column=6,sticky=W,padx=5)

pl13=Label(inner_frame,text='NT.499',font=('Inter',10),fg='#000000')
pl13.grid(row=4,column=6,sticky=W,padx=5)

pl14=Label(inner_frame,text='NT.150',font=('Inter',10),fg='#000000')
pl14.grid(row=4,column=6,sticky=W,padx=5)

pl15=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
pl15.grid(row=4,column=6,sticky=W,padx=5)

pl16=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
pl16.grid(row=4,column=6,sticky=W,padx=5)

pl17=Label(inner_frame,text='404',font=('Inter',10),fg='#000000')
pl17.grid(row=4,column=6,sticky=W,padx=5)


mb1=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl1,pl1))
mb1.grid(row=4,column=1,sticky=W)
numl1=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl1.grid(row=4,column=1)
ab1=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl1,pl1))
ab1.grid(row=4,column=1,sticky=E)

mb2=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl2,pl2))
mb2.grid(row=4,column=3,sticky=W)
numl2=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl2.grid(row=4,column=3)
ab2=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl2,pl2))
ab2.grid(row=4,column=3,sticky=E)

mb3=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl3,pl3))
mb3.grid(row=4,column=5,sticky=W)
numl3=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl3.grid(row=4,column=5)
ab3=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl3,pl3))
ab3.grid(row=4,column=5,sticky=E)

mb4=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb4.grid(row=4,column=7,sticky=W)
numl4=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl4.grid(row=4,column=7)
ab4=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab4.grid(row=4,column=7,sticky=E)

mb5=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb5.grid(row=4,column=7,sticky=W)
numl5=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl5.grid(row=4,column=7)
ab5=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab5.grid(row=4,column=7,sticky=E)

mb6=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb6.grid(row=4,column=7,sticky=W)
numl6=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl6.grid(row=4,column=7)
ab6=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab6.grid(row=4,column=7,sticky=E)

mb7=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb7.grid(row=4,column=7,sticky=W)
numl7=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl7.grid(row=4,column=7)
ab7=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab7.grid(row=4,column=7,sticky=E)

mb8=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb8.grid(row=4,column=7,sticky=W)
numl8=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl8.grid(row=4,column=7)
ab8=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab8.grid(row=4,column=7,sticky=E)

mb9=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb9.grid(row=4,column=7,sticky=W)
numl9=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl9.grid(row=4,column=7)
ab9=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab9.grid(row=4,column=7,sticky=E)

mb10=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb10.grid(row=4,column=7,sticky=W)
numl10=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl10.grid(row=4,column=7)
ab10=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab10.grid(row=4,column=7,sticky=E)

mb11=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb11.grid(row=4,column=7,sticky=W)
numl11=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl11.grid(row=4,column=7)
ab11=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab11.grid(row=4,column=7,sticky=E)

mb12=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb12.grid(row=4,column=7,sticky=W)
numl12=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl12.grid(row=4,column=7)
ab12=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab12.grid(row=4,column=7,sticky=E)

mb13=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb13.grid(row=4,column=7,sticky=W)
numl13=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl13.grid(row=4,column=7)
ab13=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab13.grid(row=4,column=7,sticky=E)

mb14=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb14.grid(row=4,column=7,sticky=W)
numl14=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl14.grid(row=4,column=7)
ab14=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab14.grid(row=4,column=7,sticky=E)

mb15=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb15.grid(row=4,column=7,sticky=W)
numl15=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl5.grid(row=4,column=7)
ab15=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab15.grid(row=4,column=7,sticky=E)

mb16=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb16.grid(row=4,column=7,sticky=W)
numl16=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl16.grid(row=4,column=7)
ab16=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab16.grid(row=4,column=7,sticky=E)

mb17=Button(inner_frame,text='-',font=('Inter',12),command=lambda: minus(numl4,pl4))
mb17.grid(row=4,column=7,sticky=W)
numl17=Label(inner_frame,text='0',font=('Inter',12,'bold'),fg='#000000')
numl17.grid(row=4,column=7)
ab17=Button(inner_frame,text='+',font=('Inter',12),command=lambda: add(numl4,pl4))
ab17.grid(row=4,column=7,sticky=E)







detaillistbutton=Button(inner_frame,text='詳細清單',font=('Inter',18),fg='#1E1E1E',bg='#ECEDE7',command=showdetail)


cartimg=Image.open('C:/Users/Harrison/Documents/Python2023spring/project/Screenshot 2023-03-26 212121.png')
cartimg=cartimg.resize((30,30))
cartimg=ImageTk.PhotoImage(cartimg)
shoppingcartlabel=Label(inner_frame,image=cartimg,width=30,height=30)

totalval=StringVar()
totalval.set('共消費:0元') 
totallabel=Label(inner_frame,textvariable=totalval,font=('Inter',10),fg='#000000')
checkoutbutton=Button(inner_frame,text='結帳',font=('Inter',18),fg='#1E1E1E',bg='#ECEDE7',command=sell)

home.rowconfigure(5,weight=2)
shoppingcartlabel.grid(row=5,column=5,sticky=E+S)
totallabel.grid(row=5,column=6,columnspan=2,sticky=W+S)
checkoutbutton.grid(row=5,column=7,sticky=E+S)
detaillistbutton.grid(row=5,column=0,sticky=S+W,padx=5,pady=1)

home.mainloop()
