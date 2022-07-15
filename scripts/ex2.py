import re

from bs4 import BeautifulSoup
import requests

date_looked_for = '2022-02-07 14:03'
url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
webpage = requests.get(url)

soup = BeautifulSoup(webpage.content, 'html.parser')
# print(soup)
files_to_scrape = []
csv = 'csv'
for child in soup.find_all('tr'):
    if child.text.__contains__(date_looked_for):
        # print(child.text.replace(date_looked_for, ' '))
        csv_name, csv, to_be_removed = child.text.partition('csv')
        files_to_scrape.append(csv_name + 'csv')


print(files_to_scrape)
