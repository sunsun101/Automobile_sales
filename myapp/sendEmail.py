import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def send(email,pwd,subject,message):

	email_user = email
	email_password = pwd
	email_send = 'shristy71078@gmail.com'

	subject = subject

	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = email_send
	msg['Subject'] = subject

	body = message
	msg.attach(MIMEText(body,'plain'))

	# filename='filename'
	# attachment  =open(filename,'rb')

	# part = MIMEBase('application','octet-stream')
	# part.set_payload((attachment).read())
	# encoders.encode_base64(part)
	# part.add_header('Content-Disposition',"attachment; filename= "+filename)

	# msg.attach(part)
	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user,email_password)


	server.sendmail(email_user,email_send,text)
	server.quit()
	return 'success'