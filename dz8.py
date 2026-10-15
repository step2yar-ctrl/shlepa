


class Book:
    def __init__(self, title, author, year, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating

    def show_info(self):
        print("Назва:", self.title)
        print("Автор:", self.author)
        print("Рік:", self.year)
        print("Рейтинг:", self.rating)


book1 = Book("Dune", "Frank Herbert", 1965, 8.8)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, 9.2)

book1.show_info()
print()
book2.show_info()




class Game:
    def __init__(self, title, genre, level, health):
        self.title = title
        self.genre = genre
        self.level = level
        self.health = health

    def show_info(self):
        print("Гра:", self.title)
        print("Жанр:", self.genre)
        print("Рівень:", self.level)
        print("Здоров'я:", self.health)


game1 = Game("Minecraft", "Sandbox", 15, 100)
game2 = Game("Cyberpunk 2077", "RPG", 20, 80)

print()
game1.show_info()
print()
game2.show_info()




class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def show_info(self):
        print("Назва:", self.title)
        print("Жанр:", self.genre)
        print("Рейтинг:", self.rating)

    def update_rating(self, new_rating):
        self.rating = new_rating


movie1 = Movie("Interstellar", "Sci-Fi", 8.7)
movie2 = Movie("Inception", "Sci-Fi", 8.8)

print()
movie1.show_info()

movie1.update_rating(9.0)
print("Новий рейтинг:", movie1.rating)

movie1.show_info()

print()
movie2.show_info()
