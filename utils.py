import requests
import re
site_data = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
site_data = site_data.text

conversion = {}
site_data = site_data.split('</Valute>')

pattern = re.compile(".*\<CharCode\>(.*)\<\/CharCode\>.*\<Value\>(.*)\<\/Value\>")
said_date = re.compile(".*Date=(.*)\sname")


for el in site_data:
    match = re.search(pattern, el)
    if match:
        conversion.update({match.group(1) : match.group(2)})
    current_date = re.search(said_date, el)
    if current_date:
        said_date = current_date.group(1)


def currency_rates(currencies):
    currencies = currencies.upper()
    print(f"Данные валют актуальны на {said_date}")
    if currencies in conversion:
        return conversion[currencies]
    else:
        return None