while True:
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))

        print("Оберіть операцію: +, -, *, /")
        op = input("Операція: ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            raise ValueError("Невідома операція!")

    except ValueError as e:
        print("Помилка:", e)
    except ZeroDivisionError:
        print("Помилка: ділення на нуль!")
    else:
        print("Операцію успішно виконано!")
        print("Результат:", result)
    finally:
        print("Калькулятор завершив обчислення.")

    again = input("Хочете виконати ще одне обчислення? (так/ні): ")
    if again.lower() != "так":
        print("Роботу калькулятора завершено.")
        break