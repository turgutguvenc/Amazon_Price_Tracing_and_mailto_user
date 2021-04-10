# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:31:15 2021

@author: turgu
"""
"""The program trace specific product which you choose then can send mail to you
when price is low """
import time
import requests
from bs4 import BeautifulSoup
import smtplib
# which product do you want to follow please enter its url in amazon.
URL = 'https://www.amazon.com/All-new-Kindle-Oasis-now-with-adjustable-warm-light/dp/B07L5GDTYY/ref=p13n_ds_purchase_sim_1p_dp_desktop_2?pd_rd_w=vgJQv&pf_rd_p=aa96da76-5f67-44bb-853b-5d14d66e2ec7&pf_rd_r=094DJ9XYE23XNW17XBNT&pd_rd_r=87951b42-8285-48f9-adb0-04e49ce5a572&pd_rd_wg=Gz38D&pd_rd_i=B07L5GDTYY&psc=1'
headers = ({
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    'Accept-Language': 'en-US'
}) 
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'lxml')


def get_title(soup):
     
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
 
        # Inner NavigatableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip()
 
        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()
 
    except AttributeError:
        title_string = ""   
 
    return title_string

def get_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
 
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
 
        except:     
            price = ""  
 
    return float(price[1:-1].replace(",","."))

def send_email(toMail, url):
    """Send e mail to mail given mail adresses"""
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls() # start this processes
    server.ehlo()
    

    
    server.login("example@gmail.com","your_password")
    
    subject = 'The product price is down!!!'
    body = 'Product link: ' + url
    msg = f'Subject:  {subject} \n\n{body}'
    
    server.sendmail("example@example.com",
                    toMail,
                    msg
                    )
    print("The message has sent.")
    server.quit()
    
def main():
    while True:
        #You can arrange the price
        if get_price(soup) < 300:
            send_email("example@icloud.com",URL)
        else: 
            print("The product price hasn't down ")
       time.sleep(60)     
if __name__ == '__main__':
    main()
    


 
    
