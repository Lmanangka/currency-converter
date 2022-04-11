'''
Author  : Leo Manangka
Created : 04/04/2022
Revision: 12/05/2022
'''

import sys
import requests

OPT = sys.argv

def help_text():
    print(f'''
    Usage:

    pyhton3 {OPT[0]} [OPTION] [currency1] [currency2] [amount]

    Option:
      -l | --list       Show latest currencies conversion rates
      -e | -- exchange  Show exchange result between currency1 and currency2
      -h | --help       Show help text
    ''')

class Currency:
    '''
    make class name currency
    '''
    def __init__(self):
        self.URL = 'https://v6.exchangerate-api.com/v6/'
        self.API_KEY = '5ead311e137e819416723196'

    def list_currenciesRate(self):
        '''
        create a function to show currencies conversion rates based on USD
        '''
        endpoint = f'{self.API_KEY}/latest/USD'
        resp = requests.get(f'{self.URL}{endpoint}')
        data = resp.json()
        return data

    def exchange(self, currency1=None, currency2=None, amount=None):
        '''
        create function to show exchange result between currency1 and currency2
        '''
        endpoint = f'{self.API_KEY}/pair/{currency1}/{currency2}/{amount}'
        if currency1 == None or currency2 == None or amount == None:
            help_text()
            sys.exit()
        else:
            resp = requests.get(f'{self.URL}{endpoint}')
            data = resp.json()
            data = f'{currency1} to {currency2}: {round(data["conversion_result"],2)}\nlast update: {data["time_last_update_utc"]}'
            return data

if __name__=='__main__':
    currency = Currency()
    try:
        if len(OPT) < 2:
            help_text()
            sys.exit()

        elif OPT[1] in {'-l', '--list'}:
            #Convert dictionary in json to list and sorted
            conversion_rates = list(currency.list_currenciesRate()["conversion_rates"].items())
            conversion_rates.sort()
            #print name and value in beautiful format
            for code, val in conversion_rates:
                print(f'{code}:', round(val,2))
            print(f'last update: {currency.list_currenciesRate()["time_last_update_utc"]}')

        elif OPT[1] in {'-e', '--exchange'}:
            #print conversion result and last update
            print(currency.exchange(str(OPT[2]), str(OPT[3]), OPT[4]))

        else:
            help_text()

    except KeyboardInterrupt:
        sys.exit()
    finally:
        sys.exit()
