#5.1
N = int (input ("Введите количество слов - "))
b = ""
for x in range (N):
    a = input ("Введите слово - ")
    b += a + " "
print (b)

#5.2
h = ""
s = 0
while s == 0:
    n = input("Введите слово или введите stop для прекращения - ")
    if n.lower == "stop":
        s = 1
        print (h)
    else:
      h += n + " "

#5.3
word = input ("Введите слово - ")
for x in word:
    if x == "Ф" or x == "ф":
        print ("Ого! Это редкое слово!")
        break
else:
    print ("Эх, это не очень редкое слово")

#5.4
import random
true = 0
false = 0
while false < 3:
    number1 = random.randint (1,10)
    number2 = random.randint (1,10)
    print(number1, "+", number2, "=", end=(' '))
    summa = int (input())
    if summa == number1 + number2:
        true += 1
        print ("Правильно")
    else:
        false += 1
        print ("Ответ неверный")
print ("Игра окончена. Правильных ответов: ", true)