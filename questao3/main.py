import requests


r = requests.get('http://coopertotal.nc7i.app/', auth=('leonardo@coopertotal.com.br', '1234'))

print(r.status_code)
print(r.text)
print(r.json())
