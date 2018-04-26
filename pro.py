from gpiozero import MotionSensor
import time
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


pir = MotionSensor(22)
time.sleep(3)
a=""

def mai():
    fromaddr = "raspiduino17300@gmail.com"
    toaddr = "madhoshmanikandan@gmail.com"
  
# instance of MIMEMultipart
    msg = MIMEMultipart()
 
# storing the senders email address  
    msg['From'] = fromaddr
 
# storing the receivers email address 
    msg['To'] = toaddr
 
# storing the subject 
    msg['Subject'] = a
 
# string to store the body of the mail
    body = "there is"+a
 
# attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
 
# open the file to be sent 
    filename = "cesea2.jpg"
    attachment = open("/home/pi/Desktop/cesea2.jpg", "rb")
 
# instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
 
# To change the payload into encoded form
    p.set_payload((attachment).read())
 
# encode into base64
    encoders.encode_base64(p)
  
    p.add_header('Content-Disposition', "attachment; /home/pi/Desktop/cesea2.jpg= %s" % filename)
 
# attach the instance 'p' to instance 'msg'
    msg.attach(p)
 
# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
    s.starttls()
 
# Authentication
    s.login(fromaddr, "parammadman420")
 
# Converts the Multipart msg into a string
    text = msg.as_string()
 
# sending the mail
    s.sendmail(fromaddr, toaddr, text)
 
# terminating the session
    s.quit()
while True:
    if pir.motion_detected:
        print("Motion Detected")
        os.system("fswebcam -F 3 --fps 20 -r 1920*1440 /home/pi/Desktop/cesea2.jpg")
        a="intruder"
        print (a)
        mai()
        print("intruder alert")
    elif (GPIO.input(4) ==1):
        os.system("fswebcam -F 3 --fps 20 -r 1920*1440 /home/pi/Desktop/cesea2.jpg")
        a="fire in the house"
        print (a)
        mai()
        sleep(2)
    else:
        print("no motion to capture")
        sleep(2)


