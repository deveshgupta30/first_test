import smtplib                                #inports smtplib to access the E-Mail server
import getpass                                #imports getpass library for hiding the password
#Beginning of UI

print("Welcome to the E-mail scheduling app.")
sender=input("Please Enter your G-Mail ID: ")
reciever=input("Please Enter the E-Mail you are sending to: ")
p=""    #password input
print("Trying to login.....")

try:                                            #Tries to access the E-mail account 
    server = smtplib.SMTP('smtp-mail.outlook.com',587)
    server.starttls()
    server.login(sender,str(p))
    print("Login Successful!")
    msg=input("Enter your message: ")
    server.sendmail(str(sender),str(reciever),msg)
    server.close()
except:
    print("E-mail not sent/Login Failed.")      #if it fails to access
    input("Press <Enter> to continue.")
else:
    print("Succesfully sent!")                  #upon successful completion of the program
input("Press <Enter> to continue.")
