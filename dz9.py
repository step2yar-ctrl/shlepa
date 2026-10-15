


class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def show_info(self):
        print("Назва:", self.title)
        print("Жанр:", self.genre)
        print("Рік:", self.year)
        print("Рейтинг:", self.rating)

    def update_rating(self, new_rating):
        self.rating = new_rating


movie1 = Movie("Interstellar", "Sci-Fi", 2014, 8.7)
movie2 = Movie("The Batman", "Action", 2022, 7.8)

movie1.show_info()
print()
movie2.show_info()

print("\nЗміна рейтингу:")
print("Поточний рейтинг:", movie1.rating)
movie1.update_rating(9.1)
print("Новий рейтинг:", movie1.rating)
movie1.show_info()




class Robot:
    def __init__(self, name, model, battery, tasks):
        self.name = name
        self.model = model
        self.battery = battery
        self.tasks = tasks

    def show_info(self):
        print("Робот:", self.name)
        print("Модель:", self.model)
        print("Батарея:", str(self.battery) + "%")
        print("Виконано завдань:", self.tasks)

    def work(self):
        print("Робот виконує завдання...")
        self.tasks += 1
        self.battery = max(0, self.battery - 10)
        self.show_info()

    def charge(self):
        self.battery = min(100, self.battery + 20)
        print("Робот заряджається...")
        self.show_info()


robot = Robot("R-01", "Helper", 80, 3)

print("\nРобот:")
robot.show_info()
robot.work()
robot.charge()




class Scooter:
    def __init__(self, model, speed, battery, mileage):
        self.model = model
        self.speed = speed
        self.battery = battery
        self.mileage = mileage

    def show_info(self):
        print("Модель:", self.model)
        print("Швидкість:", self.speed, "км/год")
        print("Заряд:", str(self.battery) + "%")
        print("Пробіг:", self.mileage, "км")

    def ride(self, distance):
        self.mileage += distance
        self.battery = max(0, self.battery - distance)
        print("Самокат проїхав", distance, "км")
        self.show_info()

    def charge(self):
        self.battery = min(100, self.battery + 20)
        print("Самокат заряджено")
        self.show_info()


scooter1 = Scooter("KuKirin G2", 45, 90, 100)
scooter2 = Scooter("KuKirin G4", 70, 80, 50)

print("\nПерший самокат:")
scooter1.show_info()
scooter1.ride(10)
scooter1.charge()

print("\nДругий самокат:")
scooter2.show_info()
scooter2.ride(5)
