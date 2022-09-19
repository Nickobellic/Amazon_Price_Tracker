import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = "https://www.amazon.com/Dell-5520-15-6-Gaming-Laptop/dp/B09YBQYJLS/ref=sr_1_1?crid=2ODPUGOCAX4OA&keywords=dell+g15+16+gb+ram&qid=1663476945&s=computers-intl-ship&sprefix=dell+g15+16+gb+ra%2Ccomputers-intl-ship%2C257&sr=1-1"
access = requests.get(url=PRODUCT_URL, headers={'User-Agent': 'agent', 'Accept-Language': 'language', 'Cookie': 'cookie'}).text

soup = BeautifulSoup(access, 'html.parser')
price_with_dollars = soup.find(name='span', class_='a-offscreen').text
price = ''
product = soup.title.text

for i in price_with_dollars:
    if i not in ['$',',']:
        price += i
price = float(price)

my_email = "mail id"
passw = "password"
smtp = smtplib.SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login(user=my_email, password=passw)
if price < 1300.00:
    message = f"\n{product} is now {price_with_dollars}"
    smtp.sendmail(from_addr=my_email, to_addrs="mail", msg=message.encode('utf-8'))
    smtp.sendmail(from_addr=my_email, to_addrs=my_email, msg=message.encode('utf-8'))
smtp.close()