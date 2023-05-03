import requests
import pygsheets
import pandas as pd
#不貸條件
r=requests.get('https://www.google.com/')
res=requests.get('https://api.exchangerate-api.com/v4/latest/TWD')
data=res.json()
a=data['rates']['USD']
b=data['rates']['JPY']
c=data['rates']['HKD']

gc= pygsheets.authorize(service_file='class7/agile-sanctum-383208-331018fe6b18.json')
#連接試算表
sht=gc.open_by_url('https://docs.google.com/spreadsheets/d/1zxVEfCazGUrcKpLqp104t0zmGFAjgCZ3WTRK1iPGOfw/edit#gid=0')
#利用INDEX選取工作表
ws=sht[0]
#利用工作表名稱尋找工作表
ws=sht.worksheet_by_title('工作表1')
#讀取表中內容
value=ws.get_value('A1')
#dataframe to work sheet
d={'country':['美國','日本','香港'],'匯率':[a,b,c]}
df=pd.DataFrame(d)
ws.set_dataframe(df,'A1')
# #有待條件
# payload={'key1':'value1','key2':'value2'}
# r=requests.get('https://www.google.com/',params=payload)
print(r.status_code)#列出HTTP狀態碼
# r=requests.post('',data={'key':'value'})