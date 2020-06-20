import smtplib
from email.mime.text import MIMEText
print("Created by Sagar B Patel......")
def alertMe(subject,body):
    myAddress="your email address"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = myAddress
    msg['Reply-to'] = myAddress
    msg['To'] = myAddress

    server=smtplib.SMTP('smtp.gmail.com',587);
    server.starttls()
    server.login(myAddress,'your password')
    server.sendmail(myAddress,myAddress,msg.as_string())
    server.quit()
alertMe("Alert!","Garage Door is Open")

