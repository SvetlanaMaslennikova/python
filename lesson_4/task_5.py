# 5. (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

from requests import get
from sys import argv


def currency_rates(val):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    res = None
    if val not in content:
        return res
    else:
        for el in content.split(f'{val}')[1:]:
            for el_1 in el.split('</Value>')[:1]:
                res = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
                for el_2 in content.split('Date="')[1:]:
                    print(el_2.split('"')[0])
                    return f'Курс валюты: {res} руб.'


if __name__ == '__main__':
    if len(argv) > 1:
        for curr in argv[1:]:
            print(currency_rates(curr))


