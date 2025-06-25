import re

# Пошук першого входження шаблону
# re.search()

text = "Привіт, мене звати Богдан і мій номер +380991234567"

match = re.search(r"\+380\d{9}", text)
if match:
    print("Знайдено номер:", match.group())



# re.match()
# Перевірка, чи початок рядка відповідає шаблону

text = "hello123"
if re.match(r"hello\d+", text):
    print("Починається з hello та цифр")


# re.findall()
# Повертає всі знайдені входження як список

text = "email1gmail.com, email2@yahoo.com"
emails = re.findall(r"\S+@\S+\.\S+", text)
print(emails)


# re.finditer()
# Те саме, що й findall, але повертає ітератор Match-об’єктів

text = "User1: test1@gmail.com, User2: demo123@mail.ru"

pattern = r"([\w.-]+)@([\w.-]+\.\w+)"  # розбиваємо на дві групи: імʼя та домен

for match in re.finditer(pattern, text):
    print(f"Знайшли email: {match.group(0)}")      # Повна відповідність
    print(f"  Імʼя: {match.group(1)}")             # Частина до @
    print(f"  Домен: {match.group(2)}")            # Частина після @
    print(f"  Позиція: {match.start()}–{match.end()}")

# re.sub()
# Заміна частини рядка, що відповідає шаблону

text = "Це тупий тест. Дуже тупий."
cleaned = re.sub(r"тупий", "розумний", text)
print(cleaned)  # Це розумний тест. Дуже розумний.ч


# re.compile()
# Створює об’єкт регулярного виразу (для багаторазового використання)


# Компілюємо шаблон
email_regex = re.compile(r"([\w.-]+)@([\w.-]+\.\w+)")

text1 = "Пошта 1: anna@gmail.com"
text2 = "Пошта 2: boss@work.ua"

# Використовуємо той самий обʼєкт у різних місцях
for txt in (text1, text2):
    match = email_regex.search(txt)
    if match:
        print(f"Email знайдено: {match.group(0)} → домен: {match.group(2)}")