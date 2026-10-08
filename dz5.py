cars = [
    ["BMW", 32000, 2020],
    ["Toyota", 24500, 2022],
    ["Audi", 41000, 2019],
    ["Tesla", 38000, 2023],
    ["Ford", 27500, 2021]
]

cars_by_price = sorted(cars, key=lambda car: car[1])
cars_by_year = sorted(cars, key=lambda car: car[2], reverse=True)

print(cars_by_price)
print(cars_by_year)


games = [
    ["Minecraft", 4.6, 95],
    ["Portal 2", 4.9, 40],
    ["Terraria", 4.7, 80],
    ["Cyberpunk 2077", 4.3, 110],
    ["Stardew Valley", 4.8, 60]
]

best_rating = max(games, key=lambda game: game[1])
longest_game = max(games, key=lambda game: game[2])

print(best_rating)
print(longest_game)


employees = [
    ["Anna", 12500, 2],
    ["Max", 18000, 5],
    ["Daniel", 15000, 3],
    ["Sofia", 22000, 7],
    ["Alex", 13500, 1]
]

employees_by_salary = sorted(
    employees,
    key=lambda employee: employee[1],
    reverse=True
)

employees_by_experience = sorted(
    employees,
    key=lambda employee: employee[2]
)

print(employees_by_salary)
print(employees_by_experience)


phones = [
    ["iPhone 15", 42000, 4.7],
    ["Samsung S24", 38000, 4.6],
    ["Google Pixel 9", 35000, 4.5],
    ["Xiaomi 14", 27000, 4.4],
    ["OnePlus 12", 30000, 4.6]
]

most_expensive = max(phones, key=lambda phone: phone[1])
best_phone = max(phones, key=lambda phone: phone[2])
phones_by_price = sorted(phones, key=lambda phone: phone[1])

print(most_expensive)
print(best_phone)
print(phones_by_price)


athletes = [
    ["Alex", 12.4],
    ["Max", 11.8],
    ["Daniel", 13.2],
    ["Anna", 11.5],
    ["Sofia", 12.1],
    ["Kate", 10.9]
]

better_than_12 = list(
    filter(lambda athlete: athlete[1] < 12, athletes)
)

better_than_12 = sorted(
    better_than_12,
    key=lambda athlete: athlete[1]
)

print(better_than_12)