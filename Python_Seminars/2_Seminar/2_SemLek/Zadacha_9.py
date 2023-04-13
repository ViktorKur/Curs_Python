# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# 1 Вариант
# num = int(input("Введите число: "))+1
# flag = 1
# if num < 0:
#     print("Введите положительное число")
# else:
#     if num == 1:
#      print("1")
#     else:
#         while num != 1:
#             flag *= num - 1
#             num -= 1
# print(flag)


# 2й Вариант
# n = int(input("Введите число :"))
# fact = 1

# while n > 1:
#     fact *= n
#     n -= 1

# print(fact)

# # 3й Вариант
# num = int(input("Введите число: "))+1
# flag = 1
# if num < 0:
#     print("Введите положительное число")
# else:
#     if num == 1:
#          print("1")
#     else:
#          while num != 1:
#              flag *= num - 1
#              num-=1
# print(flag)

# # 4й Вариант
i = int(input("Введите число :"))
fact = 1
count = 1
while i:
    fact*=count
    i-=1
    count+=1
print(fact)