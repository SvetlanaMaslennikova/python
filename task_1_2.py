# 1. Написать скрипт, создающий стартер (заготовку)
# для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера,
# чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные
# о вложенных папках и файлах (добавлять детали)?

# 2. * (вместо 1) Написать скрипт, создающий из config.yaml
# стартер для проекта со следующей структурой:
#
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#
# Примечание: структуру файла config.yaml придумайте сами,
# его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
import sys


def pos_mod_x(el_name, x):
    try:
        res = el_name.index('|--') // x
    except ValueError as e:
        print(f'Структура входного файла повреждена. Ошибка: {e}')
        sys.exit(1)
    return res


def create_el(el_name, cur_lvl):
    new_lvl = cur_lvl
    el_name = el_name[pos_mod_x(line, 1) + 3:]
    if el_name.count('.'):
        with open(el_name, 'w', encoding='utf-8'):
            pass
    else:
        try:
            os.makedirs(el_name)
        except FileExistsError:
            pass
        os.chdir(el_name)
        new_lvl += 1
    return new_lvl


f_name = 'config.yaml'
with open(f_name, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

cur_lvl = 0

for line in lines:
    if pos_mod_x(line, 3) - cur_lvl == 0:
        cur_lvl = create_el(line, cur_lvl)
    elif pos_mod_x(line, 3) - cur_lvl < 0:
        for i in range(abs(pos_mod_x(line, 3) - cur_lvl)):
            os.chdir('../')
            cur_lvl -= 1
        cur_lvl = create_el(line, cur_lvl)
    else:
        print('Нельзя создать объект на несколько уровней глубже.')
        sys.exit(1)
