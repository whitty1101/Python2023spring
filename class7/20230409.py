# from twilio.rest import Client

# account_sid = 'AC0b2c6508d3296c49ab2e41953762fff4'
# auth_token = '213e5374c9fb357cfb635aaab9574415'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     messaging_service_sid='MG4150efd04e0eabfedee4ff5449039f6e',
#   body='test',
#   to='+886938856303'
# )

# print(message.sid)



# from pathlib import Path
# p= Path('class7/20230409.py')

# print(p.resolve())


import pygsheets
import pandas as pd
#設定google cloud 用戶
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
d={'customers Name':['小明','曉華','小江'],'weight':[67,44,50]}
df=pd.DataFrame(d)
ws.set_dataframe(df,'A1')
print(df)

