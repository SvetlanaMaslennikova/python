# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

n = int(input("Введите число: "))
odd_nums = (num for num in range(1, n + 1, 2))

print(odd_nums)
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
