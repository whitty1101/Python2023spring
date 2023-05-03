import requests
#不貸條件
r=requests.get('https://www.google.com/')
res=requests.get('https://api.exchangerate-api.com/v4/latest/TWD')
data=res.json()
print('台幣對日幣的匯率為'+str(data['rates']['JPY']))

# #有待條件
# payload={'key1':'value1','key2':'value2'}
# r=requests.get('https://www.google.com/',params=payload)
print(r.status_code)#列出HTTP狀態碼
# r=requests.post('',data={'key':'value'})