# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#Мой вариант
a = int(input("Введите натуральное число А больше 1: "))
if a>1 :
  fib1=0
  fib2=1
  fibSum=0
  count=2
  flag=True
  while flag==True:
    fibSum=fib1+fib2
    fib1=fib2
    fib2=fibSum
    count+=1
    print(count,fibSum) 
    if a==fibSum:
     print(f"введенное вами число {a} является {count} по счету числом в последовательности рядя чисел Фибоначчи") 
     flag=False
    elif fibSum>a:
      print(f"введенное вами число {a} не является числом Фибоначчи -1")    
      flag=False
else :
  print("Вводимое вами число А должно быть больше 1, попробуйте ввести снова")


# n = int(input())
# a1 = 0
# a2 = 1
# i = 2
# while a2 <= n:
#   if a2 == n:
#     print(i)
#     break
# a1, a2 = a2, a1 + a2
# i += 1
# else:
# print(-1)