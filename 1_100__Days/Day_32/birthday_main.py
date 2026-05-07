from datetime import datetime
import pandas
import random
import smtplib

my_email = "vishalvanday@gmail.com"
password = "qrmonagsclbyxkiu"

import smtplib
import pandas
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("C:/Python/100_days_of_coding/1_100__Days/Day_32/birthday.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]

    file_path = "C:/Python/100_days_of_coding/1_100__Days/Day_32/bithday_text.txt"
    with open(file_path, encoding="utf-8") as f:       # 👈 Added encoding here too
        content = f.read()
        content = content.replace("[NAME]", birthdays_person["name"])

    # Build a proper MIME message
    msg = MIMEMultipart()
    msg["Subject"] = "It's the Queen's Birthday! 👑"
    msg["From"] = my_email
    msg["To"] = birthdays_person["mail"]
    msg.attach(MIMEText(content, "plain", "utf-8"))     # 👈 Declares charset explicitly

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_person["mail"],
            msg=msg.as_string()                         # 👈 Sends as a proper formatted string
        )