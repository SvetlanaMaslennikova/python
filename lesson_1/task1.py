# Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
# a) до минуты: <s> сек;
# b) до часа: <m> мин <s> сек;
# c) до суток: <h> час <m> мин <s> сек;
# d) * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input("duration = "))
days = duration // 86400
hours = duration // 3600
minutes = duration // 60
seconds = duration % 60

if duration < 60:
    print(duration, "сек")
elif 60 <= duration < 3600:
    print(minutes, "мин", seconds, "сек")
elif 3600 <= duration < 86400:
    print(hours, "час", minutes - hours * 60, "мин", seconds, "сек")
else:
    print(days, "дн", hours - days * 24, "час", minutes - hours * 60, "мин", seconds, "сек")
