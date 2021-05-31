
import json
import smtplib, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtp_address = {'gmail':"smtp.gmail.com",
            "outlook":"smtp-mail.outlook.com",
            "yahoo":"smtp.mail.yahoo.com",
            "aol":"smtp.aol.com"}


senderEmail = input("input your email id: ")
password = getpass.getpass("Password: ")
recvEmail = input("input your client email id OR client emails file(json/txt): ")
#message
print("Type your multiline msg here: ")
content = MIMEMultipart()
content['From']= senderEmail
content['Subject']="Test Work"
line = 0
messageS = ""

while line <20:
    message = input() +"\n"
    if message != "\n":
        messageS= messageS +  message
    else:
        line = 19
    line+= 1


print("Ready to send Email...")
#identify smtp and user name through email
spliter = senderEmail.split("@",1)
spliter1 = spliter[1].split(".")

smtp = smtp_address.get(spliter1[0],False)

if smtp:
    def emailTo(email):
        array = email.split("@",1)
        user = array[0]
        try:
            
            msg = "Hi "+user+","+"\n"+"\t\t"+messageS
            content.attach(MIMEText(msg,"plain"))
            full_msg = content.as_string()
            server = smtplib.SMTP(smtp,587)
            server.starttls()
            server.login(senderEmail,password)
            server.sendmail(senderEmail,email,full_msg)
            server.quit()
        except:
            print("Error somethings: check this function ")
    
    if recvEmail.endswith(".json"):
        try:

            open_file = open(recvEmail,"r")
            allEmail  = json.load(open_file)
            for email in allEmail.values():
                emailTo(email=email)
                print("Email Sent Sucessfully! ")
        except:
            print(" i think ERROR on json format check line : 28 and customize it in own way; or check json file name and directory")

    elif recvEmail.endswith(".txt"):
        try:
            open_file = open(recvEmail,"r")
            all_email = open_file.readlines()
            for email in all_email:
                emailTo(email=email)
                print("Email Sent Sucessfully! ")
                 
        except:
            print(" i think ERROR on txt format check line : 39 and customize it in own way; or check  file name and directory")


    else:
        singleEmail = recvEmail
        try:
            emailTo(singleEmail)
            print("Email Sent Sucessfully! ")
        except:
            print("check line 77 or check line 35")

else:
    print("please use top level domain in sender email:  ")
    quit()

