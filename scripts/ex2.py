'''
Scraping CSV files whose date is 2022-02-07 14:03
'''

from bs4 import BeautifulSoup
import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-7]
DATA_DIR = os.path.join(BASE_DIR, 'data')

url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
webpage = requests.get(url)


def finding_files_to_be_scraped():
    date_looked_for = '2022-02-07 14:03'

    soup = BeautifulSoup(webpage.content, 'html.parser')
    files_to_scrape = []
    csv = 'csv'
    for child in soup.find_all('tr'):
        if child.text.__contains__(date_looked_for):
            csv_name, csv, to_be_removed = child.text.partition(csv)
            files_to_scrape.append(f'{csv_name}{csv}')
    return files_to_scrape


def scrape_csv_files(names_of_csv_to_be_scraped: list):
    for filename in names_of_csv_to_be_scraped:
        req = requests.get(url)
        with open(os.path.join(DATA_DIR, filename), 'wb') as file:
            for chunk in req.iter_content(chunk_size=1024):
                file.write(chunk)


def main():
    names_of_csv_to_be_scraped = finding_files_to_be_scraped()
    scrape_csv_files(names_of_csv_to_be_scraped)


if __name__ == '__main__':
    main()

