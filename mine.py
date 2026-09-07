name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))

print(f"Привіт {name}, тобі {age}!")


#2

age = int(input("Введіть ваш вік: "))

if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")


#3

import random

number = random.randint(1, 10)

for attempt in range(3):
    guess = int(input("Вгадайте число від 1 до 10: "))

    if guess == number:
        print("Ви вгадали!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви програли! Загадане число: {number}")



#4

start = int(input("Введіть число з: "))
end = int(input("Введіть число по: "))

for number in range(start, end + 1):
    print(number, end=" ")


#5

start = int(input("Введіть число з: "))
end = int(input("Введіть число по: "))

for number in range(start, end + 1):
    print(number, end=" ")