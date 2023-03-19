import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "pj.postema@gmail.com"
password = "cxxpzzjlhjnuolih"

receiver = "pj.postema@gmail.com"
context = ssl.create_default_context()

message = """Subject: first message
Hi!
How are You?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
