# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] 
# интервал от 5 до 15
# Вывод: [1, 9, 13, 14, 19]


# # 1й Вариант
# print("\033[H\033[J")
# def ArreyIndex(arr,min,max,indx):
#  for i in range(len(array)):
#     if min < arr[i] < max:
#       indx.append(i)
#  return indx

# indx=[]
# array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# minZn= int(input("Введите минимальное значение элемента массива:"))
# maxZn= int(input("Введите максимальное значение элемента массива:"))
# indexArray = ArreyIndex(array,minZn,maxZn,indx)
# print("Индексы значений лежащих в промежутке между заданными мин и макс значениями:", indexArray)

# 2й Вариант
array = [int(i) for i in input().split()]
minZn = int(input())
maxZn = int(input())
print([indexArray for indexArray, val in enumerate(array) if minZn<= val<=maxZn])

