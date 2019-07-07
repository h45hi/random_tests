import ipdb
from smtplib import SMTP
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup

URL = 'https://www.flipkart.com/boult-audio-probass-q-bluetooth-headset-mic/p/itmfez932ragxykx?pid=ACCFEZ9372HHEWEF&lid=LSTACCFEZ9372HHEWEF1JB2FO&marketplace=FLIPKART&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_3_5&otracker1=AS_Query_OrganicAutoSuggest_3_5&fm=SEARCH&iid=253d4044-d4d1-4f46-a370-49d038a61df6.ACCFEZ9372HHEWEF.SEARCH&ppt=sp&ppn=sp&ssid=438fcosrdmi1a4u81562516578795&qH=a0e0e4a87509d04c'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

def check_price():
    # ipdb.set_trace()
    title = soup.find("span", attrs = {"class":"_35KyD6"}).get_text()
    price = soup.find("div", attrs = {"class":"_1vC4OE _3qQ9m1"}).get_text()
    updated_price = price.replace(',', '')
    int_price = int(updated_price[1:5])

    print(f"{title} is now available for {int_price}")

    if int_price < 2000:
        send_mail()
    else:
        print(f"Price is still on the notch, more than 1200")

def send_mail():
    SERVER = SMTP('smtp.gmail.com', 587)
    SERVER.ehlo()
    SERVER.starttls()
    SERVER.ehlo()
    SERVER.login('kumarnisit@gmail.com', 'gyssyqmglwgtiypg')
    subject = "Price Drop Alert !!!"
    body = '''<pre>Check out the <a href = "https://www.flipkart.com/boult-audio-probass-q-bluetooth-headset-mic/p/itmfez932ragxykx?pid=ACCFEZ9372HHEWEF&lid=LSTACCFEZ9372HHEWEF1JB2FO&marketplace=FLIPKART&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_3_5&otracker1=AS_Query_OrganicAutoSuggest_3_5&fm=SEARCH&iid=253d4044-d4d1-4f46-a370-49d038a61df6.ACCFEZ9372HHEWEF.SEARCH&ppt=sp&ppn=sp&ssid=438fcosrdmi1a4u81562516578795&qH=a0e0e4a87509d04c">product</a>, 
    it has dropped below 1200</pre>'''
    message = f"{subject}\n\n{body}"
    # message = MIMEText(body ,'html')
    SERVER.sendmail('kumarnisit@gmail.com', 'nisit@printlinkindia.com', message)
    SERVER.quit()
    print(f"Email has been sent, Hurry up before stock runs out!")

check_price()
