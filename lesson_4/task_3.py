# 3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

from requests import get


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


currency_code = input("Введите код валюты (USD, EUR, GBR...): ")
print(currency_rates(currency_code))
