import requests
import lxml
from bs4 import BeautifulSoup
from smtplib import SMTP
import os
from dotenv import load_dotenv
load_dotenv('projects\price tracker\.env')

my_email=os.getenv('EMAIL')
password=os.getenv('PASS')

URL='https://www.amazon.com/Instant-Vortex-Plus-Air-Fryer/dp/B07VHFMZHJ/ref=nav_signin?crid=1KA2DNVL2LK47&keywords=air+fyer&qid=1672237796&sprefix=air+fye%2Caps%2C303&sr=8-3&claim_type=EmailAddress&new_account=1&'
header={
    'Accept-Language':'en-US,en;q=0.5',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response=requests.get(url=URL,headers=header)
response.encoding='utf-8'

soup=BeautifulSoup(response.text,'lxml')
# print(soup.title)
price=float(soup.find(name='span',class_='a-offscreen').text[1:])
print(price)

'''user's lowest price, if lower than this price then we'll send email to user'''
user_price=130
if price<user_price:
    with SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='warmachiness13@gmail.com',
                msg=f'Subject:Air Fryer Price drop alert \n\n The price for the Air Fryer is ${price}.Hurry, Buy Now'
            )


