# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой
# фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*qaqaqa-sasasa fafasa-ratara qaqaqa-sasasa
# **Ввод:** Пара-ра-рам рам-пам-папам па-ра-па-па    
#     **Вывод:** Парам пам-пам 

print("\033[H\033[J")

def lengvSlov (stih,slovar):
  count=0
  for slr in slovar: 
    count+=stih.count(slr)
  if len(stih)==count:
    return True
  else:
    return False

def glasProv(stih,slovargl):
  puhostih = list(filter(len, stih.split(' ')))
  print(str(puhostih))
  glas=[]
  for i in range(len(puhostih)):
    count1 = 0
    for sl in slovargl: 
      count1+=puhostih[i].count(sl)
    glas.append(count1)
  if sum(glas)%len(glas)==0  and sum(glas)!=0 and len(set(glas))==1:
    return 'В стихотворении есть ритм :  Парам пам-пам'
  else:
    return 'В стихотворении нет ритма :  Пам парам'  
    
slovarRu=['ё','й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю','-',' ']
slovarEn=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','-',' ']
glasnRu=['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
glasnEngl=['a', 'e', 'i', 'o', 'u', 'y']
stih=str(input("Введите стихотворение: ")).lower()

if lengvSlov(stih, slovarRu) == True:
  print(glasProv(stih, glasnRu))
elif lengvSlov(stih, slovarEn) == True:
  print(glasProv(stih, glasnEngl))
else:
  print('Стихотворение должно быть на русском или на англиском языке, фразы разделены пробелами,\nслова в фразах разделены тире, и не использовать цыфры с символами')
