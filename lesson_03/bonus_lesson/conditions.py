x = 10

if x > 0:
    print("Число додатне")
elif x < 0:
    print("Число від'ємне")
else:
    print("Це нуль")

#----------------------------------------

score = 85

if score >= 90:
    print("Ваша оцінка: A")
elif score >= 75:
    print("Ваша оцінка: B")
elif score >= 60:
    print("Ваша оцінка: C")
else:
    print("Ваша оцінка: D")

#----------------------------------------

age = 18

if age < 12:
    print("Ти дитина")
elif age < 18:
    print("Ти підліток")
else:
    print("Ти дорослий")
# ----------------------------------------

age = 25
is_student = True

if age < 12:
    print("Дитячий квиток")
elif age < 18:
    print("Підлітковий квиток")
elif age < 26 and is_student:
    print("Студентський квиток зі знижкою")
elif age < 60:
    print("Дорослий квиток")
else:
    print("Пенсійний квиток")


# IF ELIF -------------------------------

score = 92

if score >= 90:
    print("Відмінник")
elif score >= 75:
    print("Хорошист")
else:
    print("Потрібно підтягнути знання")



score = 92

if score >= 90:
    print("Відмінник")
if score >= 75:
    print("Хорошист")
else:
    print("Потрібно підтягнути знання")