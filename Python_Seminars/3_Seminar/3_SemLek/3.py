# # Дан массив, состоящий из целых чисел.
# # Напишите программу, которая подсчитает
# # количество элементов массива, больших
# # предыдущего (элемента с предыдущим номером)
# list_nums = [0, -1, 5, 2, 3]

# array = [0,-1,5,2,3]

# count = 0

# for i in range(1, len(array) - 1) :
#     if(array[i + 1] > array[i]) :
#         count += 1
    
# print(count)

list_nums = [0, -1, 5, 2, 3]
res = [list_nums[i] > list_nums[i - 1] for i in range(1, len(list_nums))]
print(sum(res))