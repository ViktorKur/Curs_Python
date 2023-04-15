list_nums = [1, 2, 3, 4, 5]
k = 6

print(list_nums)

for i in range(k):
    list_nums.insert(0, list_nums.pop())

print(list_nums)

# def shift(list_nums, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             list_nums.append(list_nums.pop(0))
#     else:
#         for i in range(steps):
#             list_nums.insert(0, list_nums.pop())

# nums = [1, 2, 3, 4, 5]
# shift(nums, 1)
# print(nums)

list_nums = [1, 2, 3, 4, 5]
k = 6

print(list_nums)

for i in range(k):
    list_nums.insert(0, list_nums.pop())

print(list_nums)