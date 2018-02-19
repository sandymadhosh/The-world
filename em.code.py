# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("emailid", "password")
 
# message to be sent
message = ("sup")
 
# sending the mail
s.sendmail("sender emailid", "recevier emailid", message)
print ("sucess")

# terminating the session
s.quit()
