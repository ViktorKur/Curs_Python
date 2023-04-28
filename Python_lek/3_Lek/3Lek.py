# def SumNum(n,y="Hello"):
#   sum=0
#   print(y)
#   for i in range(1,n+1):
#     sum+=i
#   #print(sum)
#   return sum
# print(SumNum(int(input("Введите число: ")),"Bay"))

# Функция с неограниченным количеством входящих аргументов
# def ArgsSum(*st):
#   sumArg=""
#   for i in st:
#     sumArg+=i
#   return sumArg
# print(ArgsSum("s","t","r"))
# print(ArgsSum("s","t","r","o","k","a","5"))

# # Модульность вызов функции из файла
# #1й способ импортировать нашу функцию maxZn
# import MaxAB
# print(MaxAB.maxZn(5,25))
  
# #2й способ импортировать нашу функцию maxZn
# from MaxAB import maxZn
# print(maxZn(5,40))

# #3й способ импортировать нашу функцию maxZn и временно изменить имя модуля в программе
# import MaxAB as M1
# print(M1.maxZn(105,25))



# # Расчет числа Фиббоначи с помощью функции Рекурсии
# def Fib(n):
#   if n in [1,2]:
#     return 1
#   return Fib(n-1)+Fib(n-2)

# list_1 =[]
# for i in range(1,10):
#   list_1.append(Fib(i))
# print(list_1)


# # Алгоритм быстрой сортировки чисел
# def QuickSort(array):
#   if len(array)<=1:
#     return array
#   else:
#     pivot=array[0]
#     less=[i for i in array[1:] if i<=pivot]
#     greater = [i for i in array[1:] if i>pivot]
#     return QuickSort(less)+[pivot]+QuickSort(greater)
# print(QuickSort([12,55,2,3,6,99,13,45,6,7,9,0,21,78,]))

# Алгоритм сортировки слиянием
def mergesort(nums): 
  if len(nums) > 1: 
    mid = len(nums)//2 
    left = nums[:mid] 
    right = nums[mid:] 
    mergesort(left) 
    mergesort(right)
    i = j = k = 0 
    while i < len(left) and j < len(right): 
      if left[i] < right[j]: 
          nums[k] = left[i] 
          i += 1 
      else: 
          nums[k] = right[j] 
          j += 1 
      k += 1 
    while i < len(left): 
      nums[k] = left[i] 
      i += 1 
      k += 1 
    while j < len(right): 
      nums[k] = right[j] 
      j += 1 
      k += 1 
    
num = [3,7,4,3,9,8,10] 
mergesort(num)
print(num)
