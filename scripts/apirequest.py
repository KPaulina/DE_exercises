from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()
baseurl = 'https://open.er-api.com/v6/latest/'
endpoint = 'PLN'


def main_requests(baseurl: str, endpoint: str):
    r = session.get(baseurl + endpoint)
    return r.json()


def get_exchange_rates(response):
    return response['rates']


def prase_json(response) -> list[dict]:
    currencies = ['EUR', 'USD', 'NOK']
    currency_list = []
    for currency in currencies:
        print(currency + ' ' + str(response[currency]))
        currency_info = {
            'name': currency,
            'exchange_rate': response[currency]
        }
        currency_list.append(currency_info)
    return currency_list


data = main_requests(baseurl, endpoint)
exchange_rates = get_exchange_rates(data)
currency_exchange_rate = prase_json(exchange_rates)

df = pd.DataFrame(currency_exchange_rate)
df.to_csv('exchange_rate.csv', index=False)
