import requests
ACCESS_KEY = '6a4ea1b2470a5b69d05ae6f7e9f9ae6c'

class Converter:
    def __init__(self):
        pass

    def convert_currency(self, conv_from, conv_to, amount):
        """get currency conversion from api and if status 200, returns the converted amount"""
        try:
            response = requests.get('http://api.exchangerate.host/convert', params={
                'access_key': ACCESS_KEY,
                'from':conv_from,
                'to': conv_to,
                'amount': amount
            })
            response.raise_for_status()

        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
            print(f"Status Code: {err.response.status_code}")

        else:
            data = response.json()
            converted_amount = data["result"]
            return converted_amount
        
    def supported_currencies(self):
        """returns a list of support curreny conversions"""
        response = requests.get('http://api.exchangerate.host/list', params={
            'access_key': ACCESS_KEY
            })
        if response.status_code == 200:
            data = response.json()
            supported_curr_list = data["currencies"]
            return supported_curr_list