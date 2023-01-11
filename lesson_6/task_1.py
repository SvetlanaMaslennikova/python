# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

f_name = 'nginx_logs.txt'
result = []
with open(f_name, 'r', encoding='utf-8') as f:
    for line in f:
        element = [line[:line.index('-') - 1]]
        line = line[line.index('"') + 1:]
        element.append(line[:line.index(' ')])
        element.append(line[line.index('/'):line.index('H') - 1])
        result.append(tuple(element))

print('[')
for el in result:
    print(el, end=',\n')
print(']')
