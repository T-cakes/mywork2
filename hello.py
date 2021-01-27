print ("hello world")

username = 'stephenc0303@gmail.com'
password = 'Step0303?'
toEmail = 'stephencawfield@live.ie'
message = 'hello there!'

import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(username,password)
server.sendmail(username,toEmail,message)