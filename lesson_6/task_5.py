# 5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
# Проверить работу скрипта.

import sys

f_name1 = sys.argv[1]
f_name2 = sys.argv[2]
f_name3 = sys.argv[3]

with open(f_name1, 'r', encoding='utf-8') as f1:
    with open(f_name2, 'r', encoding='utf-8') as f2:
        with open(f_name3, 'w', encoding='utf-8') as f3:
            for line1 in f1:
                line2 = f2.readline().strip()
                if not line2:
                    line2 = None
                f3.write(f'{line1.strip()}: {line2}\n')
        content = f2.readline()
        if content:
            sys.exit(1)
