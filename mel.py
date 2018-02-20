import smtplib
S=smtplib.SMTP("smtp.live.com",25)
S.starttls()
S.login("keshav.gupta@hotmail.com","")
msg=input("Enter msg:")
S.sendmail("keshav.gupta@hotmail.com","keshav_rockzz@yahoo.com",msg)
S.close()
