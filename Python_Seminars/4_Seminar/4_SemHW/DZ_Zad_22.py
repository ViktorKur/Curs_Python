#  Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах.
#  Пользователь вводит 2 числа. n — кол-во элементов первого множества.
#  m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

##1й Вариан
# print("\033[H\033[J")
# # import random
# n = int(input("Введите n — кол-во элементов первого множества: "))
# m = int(input("Введите m — кол-во элементов второго множества: "))
# a, b, c = set(), set(),  set()
# for i in range(n):
#     a.add(int(input(f"Введите {i+1} элемент 1го множества: ")))
# for j in range(m):
#     b.add(int(input(f"Введите {j+1} элемент 2го множества: ")))
# c = a.difference(b)
# c = sorted((c.union(b)))
# print(f"1е множество: {a}")
# print(f"2е множество: {b}")
# print(f"множество неповторяющихся числ 1го и 2го мн-ва по возрастанию {c} ")

#2й Вариан
print("\033[H\033[J")
import random
n = int(input("Введите n — кол-во элементов первого множества: "))
m = int(input("Введите m — кол-во элементов второго множества: "))
a, b, c = [], [], set()
for i in range(n):
  a.append((random.randint(1, 10)))
for j in range(m):
    b.append((random.randint(1, 10)))
print(f"1й неупорядоченный набор чисел: {a}")
print(f"2й неупорядоченный набор чисел: {b}")    
a,b=set(a),set(b)
c = a.difference(b)
c = sorted((c.union(b)))
print(f"Множество неповторяющихся числ 1го и 2го набора чисел по возрастанию: {c} ")
