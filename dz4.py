# 1
numbers = [i for i in range(10, 51)]
print(numbers)

# 2
tripled = [i * 3 for i in numbers]
print(tripled)

# 3
filtered = [i for i in numbers if i % 10 == 0 or i % 10 == 5]
print(filtered)

# 4
words = ["Python", "programming", "computer", "developer", "code", "algorithm"]
lengths = [len(word) for word in words]
print(lengths)

# 5
temperatures = [-10, 0, 5, 12, 18, 23, 27, 31, 36]
fahrenheit = [round(c * 9 / 5 + 32, 1) for c in temperatures]
print(fahrenheit)