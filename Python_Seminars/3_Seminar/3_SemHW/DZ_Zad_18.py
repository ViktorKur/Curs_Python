# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
print("\033[H\033[J")

#1й Вариант
# import random
# n=int(input("Введите число N – количество элементов в массиве генерируемого случайным образом: "))
# x=int(input("Введите число Х для поиска в массиве близкого к нему числа: "))
# a,min = [],n
# # a=[1,2,5,6,9]
# for i in range(n):
#   a.append(random.randint(1,n))
#   razn= abs(x-a[i])
#   if min >= razn:
#     min=razn
#     index=i
# print ("Сгенерированный массив", a)
# print(f"Число {a[index]} в данном массиве ближе по величине заданному числу {x} ")

# 2й Вариант
import random
n=int(input("Введите число N – количество элементов в массиве генерируемого случайным образом: "))
x=int(input("Введите число Х для поиска в массиве близкого к нему числа: "))
a,minPolRazn,minOtrRazn = [],n,n
# a=[1,2,3,5,6,9]
for i in range(n):
  a.append(random.randint(1,n))
  razn = x-a[i]
  if razn < 0 and minOtrRazn >= abs(razn):
    minOtrRazn=abs(razn)
    indexOtr=i
  elif razn >= 0 and minPolRazn >= abs(razn):
    minPolRazn=abs(razn)
    indexPol=i  
print ("Сгенерированный массив", a)
if minPolRazn<minOtrRazn:
  print(f"Число {a[indexPol]} в данном массиве ближайшее по величине заданному числу {x} ")
elif minPolRazn>minOtrRazn:
  print(f"Число {a[indexOtr]} в данном массиве ближайшее по величине заданному числу {x} ") 
else :
  print(f"Числа {a[indexOtr]} и {a[indexPol]} в данном массиве ближайшие по величине заданному числу {x} ")  