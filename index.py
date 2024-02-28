import smtplib

email = "sender's email address"
password = 'password' # which you got from app password of your gmail account
receiver_email = "receiver's email address"

subject = input("Subject : ")
message = input("message : ")
text = f"subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email, password)
server.sendmail(email, receiver_email, text)
print("Email was sent successfully to : " , receiver_email)
