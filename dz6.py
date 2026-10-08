import json

# 1
movie = {
    "title": "Interstellar",
    "year": 2014,
    "rating": 8.7,
    "genres": ["sci-fi", "drama", "adventure"]
}

json_string = json.dumps(movie)

print(json_string)

movie_data = json.loads(json_string)

print("Назва:", movie_data["title"])
print("Рейтинг:", movie_data["rating"])


# 2
laptop = {
    "brand": "Lenovo",
    "model": "IdeaPad",
    "price": 28000,
    "specifications": {
        "processor": "Intel Core i5",
        "ram": 16,
        "storage": 512
    }
}

with open("laptop.json", "w", encoding="utf-8") as file:
    json.dump(laptop, file, ensure_ascii=False, indent=4)

with open("laptop.json", "r", encoding="utf-8") as file:
    laptop_data = json.load(file)

print("Виробник:", laptop_data["brand"])
print("Модель:", laptop_data["model"])
print("Ціна:", laptop_data["price"])
print("Процесор:", laptop_data["specifications"]["processor"])
print("Оперативна пам'ять:", laptop_data["specifications"]["ram"], "ГБ")


# 3
playlist = {
    "name": "My Playlist",
    "creator": "Alex",
    "songs": [
        {
            "title": "Song One",
            "artist": "Artist A",
            "duration": 210
        },
        {
            "title": "Song Two",
            "artist": "Artist B",
            "duration": 185
        },
        {
            "title": "Song Three",
            "artist": "Artist C",
            "duration": 240
        }
    ]
}

with open("playlist.json", "w", encoding="utf-8") as file:
    json.dump(playlist, file, ensure_ascii=False, indent=4)

with open("playlist.json", "r", encoding="utf-8") as file:
    playlist_data = json.load(file)

print("Назва плейлиста:", playlist_data["name"])
print("Автор:", playlist_data["creator"])
print("Перша пісня:", playlist_data["songs"][0]["title"])
print("Виконавець другої пісні:", playlist_data["songs"][1]["artist"])
print("Тривалість третьої пісні:", playlist_data["songs"][2]["duration"])


# 4
trip = {
    "destination": "Lviv",
    "days": 5,
    "transport": "train",
    "hotel": {
        "name": "Central Hotel",
        "room": "double",
        "breakfast": True
    }
}

with open("trip.json", "w", encoding="utf-8") as file:
    json.dump(trip, file, ensure_ascii=False, indent=4)

with open("trip.json", "r", encoding="utf-8") as file:
    trip_data = json.load(file)

print("Місто:", trip_data["destination"])
print("Кількість днів:", trip_data["days"])
print("Готель:", trip_data["hotel"]["name"])
print("Тип номера:", trip_data["hotel"]["room"])
print("Сніданок:", trip_data["hotel"]["breakfast"])
