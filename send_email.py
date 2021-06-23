import datetime
import smtplib
import imghdr
from email.message import EmailMessage
import os
import cv2

Sender_Email = "shelarrohan570@gmail.com"
Reciever_Email = "ranebhushan786@gmail.com"
Password = "8805059731"
newMessage = EmailMessage()                         
newMessage['Subject'] = "Message From TASK-6" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Hello this is Rohan ,we done task 6!!') 

with open('rohan1/1.jpg', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage) 
print("\t\t\t\n********************** Mail Successfully Send *********************************\n")





