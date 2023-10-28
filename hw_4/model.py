import requests


class Rate:
    def __init__(self, diff=False):
        self.diff = diff
        self.url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def get_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print('Error occurred during the request:', e)

    def get_currency_with_max_rate(self):
        data = Rate.get_data(self)
        max_rate = 0
        currency_name = ''

        for currency, value in data['Valute'].items():
            if value['Value'] > max_rate:
                max_rate = value['Value']
                currency_name = value['Name']

        return currency_name

    def get_currency_rate(self, currency_code):
        data = Rate.get_data(self)

        currency_info = data['Valute'].get(currency_code)
        if currency_info is None:
            return None

        if self.diff:
            previous_value = currency_info['Previous']
            current_value = currency_info['Value']
            diff_value = current_value - previous_value
            return diff_value
        else:
            return currency_info['Value']

    def eur(self):
        return self.get_currency_rate('EUR')

    def usd(self):
        return self.get_currency_rate('USD')
