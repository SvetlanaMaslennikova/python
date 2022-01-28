# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
# что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

from sys import exit
import json

users = 'users.csv'
hobby = 'hobby.csv'
result_dict = dict()
with open(users, 'r', encoding='utf-8') as f1:
    with open(hobby, 'r', encoding='utf-8') as f2:
        for line1 in f1:
            line2 = f2.readline().strip()
            if not line2:
                line2 = None
            if line1 not in result_dict:
                result_dict[line1.strip()] = line2
        content = f2.read()
        if content:
            exit(1)

result = 'result.json'
with open(result, 'w', encoding='utf-8') as result_file:
    dict_as_string = json.dumps(result_dict, ensure_ascii=False)
    result_file.write(dict_as_string)
with open(result, 'r', encoding='utf-8') as f:
    content = f.read()
    res = json.loads(content)
print(res)
