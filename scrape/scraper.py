import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from time import sleep
from random import randint
import csv

name=[]
link=[]
pages = np.arange(1,9,1)
for page1 in pages:
    page1 = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anE'+str(page1)+'.htm')

    soup = BeautifulSoup(page1.text, 'html.parser')
    sleep(randint(2,10))
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        name.append(names)
        links = 'https://web.archive.org' + artist_name.get('href')
        link.append(links)


author=pd.DataFrame({
    'name':name,
    'link':link,


})

print(author)
author.to_csv('artists.csv')