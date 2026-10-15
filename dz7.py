
import csv

games = [
    ["Minecraft", "Sandbox", 2011, 9.0],
    ["Cyberpunk 2077", "RPG", 2020, 8.5],
    ["The Sims 4", "Simulation", 2014, 8.0],
    ["Hades", "Roguelike", 2020, 9.1]
]

with open("games.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "genre", "year", "rating"])
    writer.writerows(games)

print("1. Назви ігор та рейтинги:")

with open("games.csv", "r", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["title"], "-", row["rating"])

print("\n2. Пошук гри:")
name = input("Введіть назву гри: ")
found = False

with open("games.csv", "r", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if row["title"].lower() == name.lower():
            print("Назва:", row["title"])
            print("Жанр:", row["genre"])
            print("Рік:", row["year"])
            print("Рейтинг:", row["rating"])
            found = True

if not found:
    print("Гру не знайдено.")

print("\n3. Пошук за жанром:")
genre = input("Введіть жанр: ")
found = False

with open("games.csv", "r", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if row["genre"].lower() == genre.lower():
            print(row["title"], "-", row["rating"])
            found = True

if not found:
    print("Ігор цього жанру не знайдено.")

books = [
    ["Harry Potter", "J.K. Rowling", 1997, 9.0],
    ["Dune", "Frank Herbert", 1965, 8.8],
    ["The Hobbit", "J.R.R. Tolkien", 1937, 9.2],
    ["1984", "George Orwell", 1949, 9.1],
    ["The Little Prince", "Antoine de Saint-Exupery", 1943, 8.9]
]

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "author", "year", "rating"])
    writer.writerows(books)

print("\n4. Назви книг та автори:")

with open("books.csv", "r", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["title"], "-", row["author"])

name = input("Введіть назву книги: ")
found = False

with open("books.csv", "r", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if row["title"].lower() == name.lower():
            print("Назва:", row["title"])
            print("Автор:", row["author"])
            print("Рік:", row["year"])
            print("Рейтинг:", row["rating"])
            found = True

if not found:
    print("Книгу не знайдено.")
