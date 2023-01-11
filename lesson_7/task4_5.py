# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

# 5. * (вместо 4) Написать скрипт, который выводит статистику
# для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]),
# например:
#
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json
# в той же папке, где запустили скрипт.

import os
import sys
import json

my_dict = {0: [0, []]}
my_dict.update({10 ** i: [0, []] for i in range(1, 9)})
num_files = 0
total_files = 0

directory = str(sys.argv[0])
fold_name = (os.path.split(directory)[1])
for root, dirs, files in os.walk(directory):
    for file in files:
        num_files += 1
        for i in my_dict:
            file_size = os.stat(os.path.join(root, file)).st_size
            file_mod = os.path.splitext(file)[1]
            if (i <= file_size < i * 10) or (file_size == 0 and i == 0):
                my_dict[i][0] += 1
                if file_mod not in my_dict[i][1]:
                    my_dict[i][1].append(file_mod)
                total_files += 1

for i in my_dict:
    my_dict[i] = tuple(my_dict[i])

with open(fold_name + '_summary.json', 'w+', encoding='utf-8') as users_json:
    json.dump(my_dict, users_json)
print(my_dict)
print(num_files)
print(total_files)
