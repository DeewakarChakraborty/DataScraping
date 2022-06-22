import pandas as pd
import time

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin

start = time.time()

driver = webdriver.Chrome(
    executable_path=r"C:\Users\MAQ USER\Downloads\chromedriver") 

driver.get(
    "https://www.zomato.com/hyderabad/restaurants")  

time.sleep(6)  
scroll_pause_time = 4  
screen_height = driver.execute_script("return window.screen.height;") 
i = 1

while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, "html.parser")
divs = soup.findAll('div', class_='jumbo-tracker')

urls = []
rest_name = []
ratings = []
price = []
crusine = []
for parent in divs:  
    try:
        name_tag = parent.find("h4")
        rest_name.append(name_tag.text)
        link_tag = parent.find("a")

        base = "https://www.zomato.com"  
        if 'href' in link_tag.attrs:
            link = link_tag.get('href')
        url = urljoin(base, link)
        urls.append(url)
        rating_tag = div.div.a.next_sibling.div.div.div.div.div.div.div.text
        price_tag = div.div.a.next_sibling.p.next_sibling.text
        crusine_tag = div.div.a.next_sibling.p.text
        ratings.append(rating_tag)
        price.append(price_tag)
        crusine.append(crusine_tag)
    except:
        pass

df = pd.DataFrame({'links': urls, 'names': rest_name, 'ratings': ratings, 'price for one': price, 'crusine': crusine})

df.to_csv("Hyderabad_Resturants.csv")

print('Data scraped successfully')
driver.close()
