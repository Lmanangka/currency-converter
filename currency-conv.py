'''
Author: Leo Manangka
Created: 04/04/2022
'''

import sys
import requests
import json
URL = 'https://v6.exchangerate-api.com/v6/'
API_KEY = '5ead311e137e819416723196' 
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
def list_currenciesRate():
    '''
    create a function to show currencies conversion rates based on USD
    '''
    endpoint = f'{API_KEY}/latest/USD'
    resp = requests.get(f'{URL}{endpoint}')
    data = resp.json()
    #Convert dictionary in json to list and sorted
    conversion_rates = list(data['conversion_rates'].items())
    conversion_rates.sort()
    #print name and value in beautiful format
    for code, val in conversion_rates:
        print(f'{code}:', round(val,2))
    print(f'last update: {data["time_last_update_utc"]}')

def exchange(currency1=None, currency2=None, amount=None):
    '''
    create function to show exchange result between currency1 and currency2
    '''
    endpoint = f'{API_KEY}/pair/{currency1}/{currency2}/{amount}'
    if currency1 == None or currency2 == None or amount == None:
        help_text()
        sys.exit()
    else:
        resp = requests.get(f'{URL}{endpoint}')
        data = resp.json()
        data = f'{currency1} to {currency2}: {round(data["conversion_result"],2)}',\
                f'last update: {data["time_last_update_utc"]}'
        #print conversion result and last update
        for result in data:
            print(result)

if __name__=='__main__':
    try:
        if len(OPT) < 2:
            help_text()
            sys.exit()
        elif OPT[1] in {'-l', '--list'}: 
            list_currenciesRate()
        elif OPT[1] in {'-e', '--exchange'}:
            exchange(str(OPT[2]), str(OPT[3]), OPT[4])
        else:
            help_text()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        sys.exit()
