from datetime import date
from dateutil import parser
import re
from MFDailyDetailsCollection import MFDailyDetailsCollection

mf_daily_rate = MFDailyDetailsCollection()

def get_todays_date()->date:
    return date.today()


def get_converted_currency_rate(source_curr, target_curr):
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    return c.get_rate(source_curr, target_curr)

def get_compund_interest_rate(principal, mature_amount, times_per_year, years):
    return times_per_year * ( ((mature_amount/principal)** (1/(times_per_year*years))) - 1)
    # r = n[(A / P)1 / nt - 1]

def compound_interest(principal, rate, times_per_year, years):
    # (1 + r/n)
    body = 1 + (rate / times_per_year)
    # nt
    exponent = times_per_year * years
    # P(1 + r/n)^nt
    return principal * pow(body, exponent)

def mf_nav_value(mf_code, cal_date):
    mf_daily_rate.execute()
    return mf_daily_rate.find_from_SchemeCode(mf_code)

def stock_price(code):
    import json

    import requests

    rsp = requests.get('https://finance.google.com/finance?q={}&output=json'.format(code))

    if rsp.status_code in (200,):
        fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
        return float (fin_data['op'])

    return 1

def parse_str_to_date(str_parse)->date:
    try:
        return parser.parse(str_parse).date()
    except ValueError:
        return date.today()

def parse_str_to_float(str_parse)->float:
    if str_parse:
        s = re.sub("[^0123456789\.]", "", str_parse)
        return float(s)
    return 0.0

def parse_str_to_boolean(str_parse)->bool:
    if str_parse in ['Yes', 'yes', 'y', 'True', 'true']:
        return True
    return False

def parse_str_to_mf_name(str_parse)->str:
    return str_parse.split('-')[0].strip()

if __name__ == '__main__':
    print(parse_str_to_date('11-1-2016'))
    print(parse_str_to_date('11/1/2016'))
    print(parse_str_to_float('₹346,284.00'))
    print(parse_str_to_boolean('Yes'))
    print(parse_str_to_boolean('No'))
    print(parse_str_to_mf_name('Aditya Birla Sun Life Frontline Equity Fund - Growth - Direct Plan'))
    print(get_compund_interest_rate(50, 100, 4, 9))
    print(stock_price('WDAY'))
