# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5 Вывод: 7 9 11 13 15

print("\033[H\033[J")
# def ArifmProgres(an,a1,n,d):
#   if n<1:
#     return an
#   an.append(a1+(n-1)*d)
#   return ArifmProgres(an, a1, n-1, d) 

# an=[]
# a = int(input("Введите первый элемент арифметической прогрессии a1: "))
# d = int(input("Введите разность элементов арифметической прогрессии d: "))
# n = int(input("Введите количество элементов арифметической прогрессии n: "))
# an=ArifmProgres(an, a, n, d)
# an.reverse() 
# print(end='\n' f"Получившаяся арифметическая прогрессия из {n} элементов с разностью {d}: {an}")

# 2 Вариант :
a = int(input("Введите первый элемент арифметической прогрессии a1: "))
d = int(input("Введите разность элементов арифметической прогрессии d: "))
n = int(input("Введите количество элементов арифметической прогрессии n: "))
for i in range(n):
  print(a+i*d, end=" ")