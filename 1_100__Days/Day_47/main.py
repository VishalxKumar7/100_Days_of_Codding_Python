from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()

email = "singvishal40001@gmail.com"
password = os.environ.get("MAIL_APP_PASSWORD")

url = "https://www.amazon.in/dp/B0FC2Z19RX/ref=sspa_dk_detail_5?pd_rd_i=B0FC2Z19RX&pd_rd_w=prIeI&content-id=amzn1.sym.67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_p=67d3dec9-3503-44a1-a945-e969d04cca69&pf_rd_r=P55FM1A7WVJG0PTMWT2W&pd_rd_wg=SqYN4&pd_rd_r=70b410be-f0c7-491e-89b8-06b2d2da3156&aref=ni49L2yAg7&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find("span", class_ = "aok-offscreen")

price_without_currency = price.text.split("₹")[1].split(" ")[0]

price_in_float = float(price_without_currency)


if price_in_float < 1000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="vishalkumar8585905754@gmail.com",
                             msg="Subject: Price has droped \n\n The Buds that you were looking for is now below 1000 Rupees")
