# 2. *(вместо 1) Написать регулярное выражение для парсинга
# файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000]
# "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re
import os


def parsing_file(file):
    pattern = re.compile(r'(^.+)\s-\s-\s\[(.+)]\s"(\w+[A-Z])\s(/\w+\w+)\s.+"\s(\d+)\s(d+)\s')
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            r = pattern.finditer(line)
            for i in r:
                result.append((i.group(1), i.group(2), i.group(3), i.group(4), i.group(5), i.group(6)))
        return result


if __name__ != '__main__':
    file = 'nginx_logs.txt'
    path_file = os.path.abspath(file)
    f_list = parsing_file(path_file)
    for str in f_list:
        print(str)
