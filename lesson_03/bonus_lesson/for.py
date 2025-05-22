text = "Hello"
for char in text:
    print(char)

# -------------------------

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


# -------------------------

colors = ("red", "green", "blue")
for color in colors:
    print(color)

# -------------------------

unique_numbers = {10, 20, 30, 40}
for num in unique_numbers:
    print(num)


# -------------------------

person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(key)


# --------------------------

for i in range(5):  # Від 0 до 4
    print(i)

# ---------------------------

names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")


# ----------------------------

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")