#導入模組
#如果想要在電子郵件中加入IMG，則須在PYTHON專案中引用MIMEImage類別，並且引用pathlib函式庫來讀取圖片
#導入MIMEMULTIPART
#引入SMTPLIB
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import smtplib
#建立EMAIL物件
text=MIMEText('DEMO-Im a email from python')
#use bytes
image=MIMEImage(Path('C:/Users/Harrison/Documents/Python2023spring/logo_tree.png').read_bytes())
#建立並設定物件
content=MIMEMultipart()#建立物件
content['subject']='2023 Python APP'#郵件TITLE
content['from']='bagelcatboy@gmail.com'#寄件者
content['to']='kubetech.academy@gmail.com'#收件者
#郵件內容使用MIMEMULTIPART物件的ATTACHMETHOD進行設定
content.attach(text)#郵件內容
content.attach(image)#郵件圖片內容
#建立SMTPLIB物件
smtp=smtplib.SMTP(host='smtp.gmail.com',port='587')
#利用WITH來釋放資源
with open('C:/Users/Harrison/Documents/Python2023spring/class5/password.txt','r') as f:
    mailToken=f.read()
with smtp:#利用with來釋放資源
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('bagelcatboy@gmail.com',mailToken)
        smtp.send_message(content)
        print('email is sended completely')
        smtp.quit()
    except Exception as e:
        print('Error message:',e)





#vwouijkoghgqgaau