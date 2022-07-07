import requests
import json
from config import exchanges

class ApiException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise ApiException(f'Валюта {base} не найдена!!'
            )
        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise ApiException(f'Валюта {sym} не найдена!!')
        if base_key == sym_key:
            raise ApiException(f'Невозможно конвертировать одинаковые валюты {base}!!')
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise ApiException(f'Не удалось обработать сумму {amount}!!')

        r = requests.get(
            f'https://api.exchangerate.host/latest?base={base_key}&symbols={sym_key}&amount={amount}')
        resp = json.loads(r.content)
        new_price = resp['rates'][sym_key]
        return round(new_price, 2)