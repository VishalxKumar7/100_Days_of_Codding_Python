# ### MAIL SMTP

# import smtplib

# my_email = "singvishal40001@gmail.com"
# password = "dfjsdlkfndlsnflk"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="vishalkumar8585905754@gmail.com", msg="Subject:Hello\n\n This is the body of my email.")


import datetime

now = datetime.datetime.now()
year = now.year
month = now.month
print(type(now))
print(now)
