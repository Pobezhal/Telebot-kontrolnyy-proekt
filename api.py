import requests
import json


base_key = 'USD'
sym_key = 'RUB'

amount = 99.1

r = requests.get(f'https://api.exchangerate.host/latest?base={base_key}&symbols={sym_key}')
resp = json.loads(r.content)
new_price = resp['rates'][sym_key] * float(amount)

print(new_price)
