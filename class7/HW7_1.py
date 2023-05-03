import pygsheets
import tkinter.ttk as ttk
from tkinter import *
import pandas as pd

def enter():
    name=name1.get()
    password=password1.get()
    phonenum=phone1.get()
    email=email1.get()
    print('Name'+str(name)+'\nEmail:'+str(email)+'\nPassword:'+str(password)+'\nPhone num'+str(phonenum))
    df=pd.DataFrame(ws.get_all_records())
    df.loc[len(df.index)]=[str(name),str(email),str(password),str(phonenum)]
    print(df)
    ws.set_dataframe(df,'A1')

#設定google cloud 用戶
gc= pygsheets.authorize(service_file='class7/agile-sanctum-383208-331018fe6b18.json')
#連接試算表
sht=gc.open_by_url('https://docs.google.com/spreadsheets/d/1zxVEfCazGUrcKpLqp104t0zmGFAjgCZ3WTRK1iPGOfw/edit#gid=0')
#利用INDEX選取工作表
ws=sht[0]
#利用工作表名稱尋找工作表
ws=sht.worksheet_by_title('工作表1')
#更改表中內容



page=Tk()
page.title('page')
page.geometry('1920x1080')
namet=Label(page,text='name:  ')
namet.grid(row=0,column=0)
name1=ttk.Entry(page)
name1.grid(row=0,column=1)

emailt=Label(page,text='email:  ')
emailt.grid(row=1,column=0)
email1=ttk.Entry(page)
email1.grid(row=1,column=1)

passwordt=Label(page,text='password:  ')
passwordt.grid(row=2,column=0)
password1=ttk.Entry(page)
password1.grid(row=2,column=1)

phonet=Label(page,text='name:  ')
phonet.grid(row=3,column=0)
phone1=ttk.Entry(page)
phone1.grid(row=3,column=1)

generate=Button(page, text='enter',command=enter)
generate.grid(row=5,column=0)



page.mainloop()