"""
Author  : Leonardo Rudolf Manangka
Created : 09 January 2023
"""

import argparse
import sys
import json
#from pprint import pp
from configparser import ConfigParser
from urllib import request, error
import style

BASE_EXCHAGE_RATE_URL = "https://v6.exchangerate-api.com/v6"

def _get_api_key():
    """
    A function for retrive a API key from api_key.ini
    """
    config = ConfigParser()
    config.read("api_key.ini")
    return config["exchangerate"]["api_key"]

def read_user_input():
    """
    A function to read a user input for amount and types of currencies.
    """
    parser = argparse.ArgumentParser(prog="currency-conv",
            description="Currency converter using an API from exchangerate-api")
    parser.add_argument("amount", nargs=1, type=int, help="Enter the amount of money")
    parser.add_argument("currency", nargs=2, type=str, help="Enter the currencies types")
    return parser.parse_args()

def exchange_rate_query(currency1, currency2, amount):
    """
    A function to build a API endpoint conversion require amount of money and
    types of currencies.
    """
    api_key = _get_api_key()
    url = (f"{BASE_EXCHAGE_RATE_URL}/{api_key}/pair/{currency1.upper()}/{currency2.upper()}/{amount}")
    return url

def get_exchange_rate_data(url_query):
    """
    A function to get a data from API end point such as conversion rate,
    conversion result, and time last update, etc.
    """
    try:
        resp = request.urlopen(url_query)
    except error.HTTPError as http_error:
        if http_error.code == 401:
            sys.exit("Access denied, check your API key!!")
        elif http_error.code == 404:
            sys.exit("Can't find data for this currencies.")
        else:
            sys.exit("Something went wrong...({http_error.code})")
    data = resp.read()
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response")

def display_data(exchange_rate_data):
    """
    A function to display a data and make it more easy to read for user, such
    as conversion rate, conversion result, and time last update.
    """
    conv_rate = exchange_rate_data["conversion_rate"]
    conv_res = exchange_rate_data["conversion_result"]
    time = exchange_rate_data["time_last_update_utc"]

    style.change_color(style.REVERSE)
    style.change_color(style.WHITE)
    print(f"{round(conv_rate, 2):^{style.PADDING}}", end="")
    style.change_color(style.GREEN)
    print(f"{round(conv_res, 2):^{style.PADDING}}", end="")
    style.change_color(style.CYAN)
    print(f"{time}")
    style.change_color(style.RESET)

if __name__=="__main__":
    user_input = read_user_input()
    url_query = exchange_rate_query(user_input.currency[0],
            user_input.currency[1], user_input.amount[0])
    exchange_rate_data = get_exchange_rate_data(url_query)
#    pp(exchange_rate_data)
    display_data(exchange_rate_data)
