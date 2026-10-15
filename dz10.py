
class Device:
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year

    def show_info(self):
        print("Пристрій:", self.name)
        print("Виробник:", self.manufacturer)
        print("Рік випуску:", self.year)


device = Device("Телевізор", "Samsung", 2023)
device.show_info()


class Laptop(Device):
    def __init__(self, name, manufacturer, year, ram):
        super().__init__(name, manufacturer, year)
        self.ram = ram

    def work(self):
        print("Ноутбук працює...")

    def show_info(self):
        super().show_info()
        print("Оперативна пам'ять:", self.ram, "ГБ")


laptop = Laptop("IdeaPad", "Lenovo", 2024, 16)

print()
laptop.show_info()
laptop.work()



class Smartphone(Device):
    def __init__(self, name, manufacturer, year, memory):
        super().__init__(name, manufacturer, year)
        self.memory = memory

    def call(self):
        print("Смартфон здійснює дзвінок...")

    def show_info(self):
        super().show_info()
        print("Обсяг пам'яті:", self.memory, "ГБ")


smartphone = Smartphone("Redmi Note 13", "Xiaomi", 2024, 256)

print()
smartphone.show_info()
smartphone.call()
