# 1. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут
# длиной m километров? При решении этой задачи
# нельзя пользоваться условной инструкцией if и циклами.
#n=700 m=750 -> 2

# #1й вариант
# n = int(input("Введите 1-е расстояние "))
# m = int(input("Введите 2-е расстояние "))
# t = (m + n - 1) // n
# print(t)

# #2й вариант
n = int(input('Введите сколько километров проезжает машина за день: '))
m = int(input('Введите сколько километров надо проехать: '))
print('Машина проедет', m, 'километров за', -(-m//n), 'дня')