import smtplib, ssl




host="smtp.gmail.com"

port=465


username="superpeppino0000@gmail.com"
password= "simibxtinjspkmye"
receiver="vegnente.chiara@gmail.com"

context = ssl.create_default_context()
message="""
ciao!
come va?
ciao.
puzzi 


"""


with smtplib.SMTP("smtp.gmail.com")as server:
    server.starttls() and server.login(user=username,password=password)
    server.sendmail(from_addr=username,
                     to_addrs=receiver,
                     msg=message)
