# 2. В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.
# 20 21 22 (ввод не в одну строку) -> 32

a = int(input("Введите количество учащихся в 1м классе: "))
b = int(input("Введите количество учащихся в 2м классе: "))
c = int(input("Введите количество учащихся в 3м классе: "))
print(a//2 + b//2 + c//2 + a%2 + b%2 + c%2)
sum = ((a+1) // 2) + ((b+1) // 2) + ((c+1) // 2)
print(f"Наименьшее кол-во парт необходимое для 3х классов = {sum}")

# 2й Вариант
# stud1 = int(input("Введите количество учеников: "))
# stud2 = int(input("Введите количество учеников: "))
# stud3 = int(input("Введите количество учеников: "))

# # comp = (stud1 // 2 + stud2 // 2 + stud3 // 2 + stud1 % 2 + stud2 % 2 + stud3 % 2)
# # comp = -(-(stud1+stud2+stud3)//2)
# comp = -((-stud1//2) + (-stud2//2) + (-stud3//2))
# print(f"наименьшее число парт, которое нужно приобрести для них {comp}")