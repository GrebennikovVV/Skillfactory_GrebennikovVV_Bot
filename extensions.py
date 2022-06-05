import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Выбраны одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не известная мне валюта {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не известная мне валюта {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')


        headers = {
            "apikey": "UMACho2NHdRhp8bN8pcxY0Af4MtSdCLP"
        }

        url = f'https://api.apilayer.com/currency_data/convert?to={quote_ticker}&from={base_ticker}'
        r = requests.request("GET", url, headers=headers)
        total_base = json.loads(r.text)[keys[base]]

        return total_base
