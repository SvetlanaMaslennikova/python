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
# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

f_name = 'nginx_logs.txt'
result = []
logs_dict = dict()
with open(f_name, 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        ip = ln[0]
        result.append((ip, ln[5].strip('"'), ln[6]))
        if ip not in logs_dict:
            logs_dict[ip] = 1
        else:
            logs_dict[ip] += 1
print('[')
for el in result:
    print(el, end=',\n')
print(']')

m = 0
k = ''
for key, value in logs_dict.items():
    if value > m:
        m = value
        k = key
print(k, m)
