import smtplib
import datetime as dt
import random

my_email = "singvishal40001@gmail.com"
password = "nleuvdarusbmuuap"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("C:/Python/100_days_of_coding/1_100__Days/Day_32/quotes.txt") as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs="vishalkumar8585905754@gmail.com",
                             msg=f"Subject: Wednessday Motivation\n\n {quote}")

