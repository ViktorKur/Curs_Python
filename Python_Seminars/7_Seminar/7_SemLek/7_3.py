# ; Задача №51. Решение в группах Напишите функцию same_by(characteristic, objects), 
# ; которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# ; и возвращают True, если это так. Если значение характеристики для разных объектов отличается
# ; - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент 
# ; characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# ;  Ввод:
# ;  values = [0, 2, 10, 6]
# ;   if same_by(lambda x: x % 2, values):
# ;       print(‘same’) 
# ;   else: print(‘different’)
# ;   Вывод: same

# def same_by(character, obj):
#    return len(set(map(character,obj)))==1

# values = [0, 2, 10, 6,1]
# if same_by(lambda x: x % 2, values):
#   print("same") 
# else:
#   print('different')
  
  
# # упрощенный вариант предыд программы и будет возвращать или тру или фолс
# print(len(set(map(lambda x: x % 2,[2, 3, 6, 4])))==1)
# # 0 1 0 0
# # (0,1)

# 2Й Вариант

def same_by(f,a):
  for i in a:
    if f(i):
      return False
  else:
    return True

print(same_by(lambda x: x % 2,[2, 3, 6, 4]))