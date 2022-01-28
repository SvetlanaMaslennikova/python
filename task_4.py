# 4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from sys import exit
import json

users = 'users.csv'
hobby = 'hobby.csv'
users_hobby = 'users_hobby.txt'

with open(users, 'r', encoding='utf-8') as f1:
    with open(hobby, 'r', encoding='utf-8') as f2:
        with open(users_hobby, 'w', encoding='utf-8') as f3:
            for line1 in f1:
                line2 = f2.readline().strip()
                if not line2:
                    line2 = None
                f3.write(f'{line1.strip()}: {line2}\n')
            content = f2.readline()
            if content:
                exit(1)
