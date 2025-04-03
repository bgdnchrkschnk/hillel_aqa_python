for num in range(1, 6):
    if num == 3:
        continue  # Пропускає число 3 і переходить до наступної ітерації
    print(num)

for num in range(1, 6):
    if num == 3:
        break  # Зупиняє цикл на числі 3
    print(num)

# --------------------------

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # Пропускає число 3
    print(x)


x = 0
while x < 5:
    x += 1
    if x == 3:
        break  # Зупиняє цикл
    print(x)

# ----------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num % 2 == 0:  # Якщо число парне, пропускаємо його
        continue
    print(num)


# ------------------------------

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
    {"name": "David", "active": False}
]

for user in users:
    if not user["active"]:  # Якщо користувач не активний, пропускаємо його
        continue
    print(user["name"])

# ----------------------------------

sentences = [
    "I love Python",
    "JavaScript is cool",
    "Python is amazing",
    "I enjoy coding in Java"
]

for sentence in sentences:
    if "Python" not in sentence:  # Якщо немає слова "Python", пропускаємо
        continue
    print(sentence)