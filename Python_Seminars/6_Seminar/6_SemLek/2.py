# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.

# list1 = [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
# list2= [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
# list3= [i for i in list1  if i not in list2]

# print(list1)
# print(list2)
# print(list3)

list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
list_k = [i for i in range(1, len(list_n) - 1) if list_n[i - 1] < list_n[i] > list_n[i + 1]]
print(list_k)