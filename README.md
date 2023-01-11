# Currency Converter

This project using python to retrive data from an API, this is part of my
learning to implemented API in practical used and know more about how API work.
For this project I used a free exchange rate API from exchangerate-api,
they over for free user 1500 calls every month. For future development I'll
try to make a graphical user interface using Kivy so user have an option to
using CLI interface or GUI.

## How To Use

- To show a help message use this command

```sh
python currency-conv.py -h
```

![image of currency converter help message](https://github.com/Lmanangka/currency-converter/blob/main/img/currency-conv_help_message.png?raw=true)

- To convert a currency use this command

```sh
python currency-conv.py amount currency currency
```

- Example

```sh
python currency-conv.py 5 USD IDR
```

![image of currency converter uppercase](https://github.com/Lmanangka/currency-converter/blob/main/img/currency-conv_uppercase.png?raw=true)

or

```sh
python currency-conv.py 5 usd idr
```

![image of currency converter lowercase](https://github.com/Lmanangka/currency-converter/blob/main/img/currency-conv_lowercase.png?raw=true)

upper or lower case are ignored, it will convert 5 USD to Indonesia IDR and
it will also showed a last update in UTC.

## Credits

- [Build Command-line Interfaces with argparse](https://realpython.com/command-line-interfaces-python-argparse/)
- [Make a good CLI interface and using API](https://realpython.com/build-a-python-weather-app-cli/)
- [Exchange rate API](https://www.exchangerate-api.com/)
