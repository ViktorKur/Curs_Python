# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

print("Задумайте два натуральных числа X и Y (X,Y≤1000)")
sum=int(input("Введите первую подсказку, ввиде суммы этих чисел S: "))
pr=int(input("Введите вторую подсказку, ввиде произведения этих чисел Р: "))
for i in range(1000):
  if i<pr:
    razn = sum-i
    if pr==(razn)*i:
      print (f"Первое задуманое Вами число = {i} и второе = {razn}")
      break
  else:
    print ("Похоже Вы мухлюете или ошибочно дали не верные подсказки, давайте попробуем заново ;)")
    break
    