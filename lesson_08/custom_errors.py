class CustomValidationError(Exception):
    ...
#
class CustomValidationError3(Exception):
    pass
#
# # class CustomValidationError2(Exception):
# #     def __init__(self, message):
# #         self.message = message
# #         message = f"This message is custom for - {self.message}"
# #         super().__init__(message)
#
#
#
def enter_user_age(age: int):
    if 18 > age > 0:
        print("access is not allowed")
    elif age <= 0:
        raise CustomValidationError("age can't be negative or zero")
    else:
        print("Access allowed!")


list_of_ages: list[int] = [28, 16, 0, 13, -21]
try:
    for age in list_of_ages:
        enter_user_age(age)
except Exception as e:
    ...




#
# users_list = [
#     {"name": "Bohdan",
#      "age": 18},
#     {"name": "Den",
#      "age": 13},
#     {"name": "James",
#      "age": -27}
# ]
#
# try:
#     for user in users_list:
#         enter_user_age(user["age"])
#         print(f"success for {user}")
# except CustomValidationError as e:
#     print(f"Skipping this value, {e}")
# else:
#     print("All done without fails!")
# finally:
#     print("finally processed.")
#
#
#
#
# try:
#     raise CustomValidationError3
# except ValueError as e:
#     ...
# else:
#     print("else")
# finally:
#     print("finally")

# class TooLargeValueError(Exception):
#     def __init__(self, value, limit):
#         self.value = value
#         self.limit = limit
#         message = f"Значення {value} перевищує ліміт {limit}"
#         super().__init__(message)
#
# # Приклад використання власного виключення
# try:
#     limit = 100
#     user_input = int(input("Введіть число: "))
#
#     if user_input > limit:
#         raise TooLargeValueError(user_input, limit)
#     else:
#         print("Дякую! Ви ввели припустиме значення.")
# except TooLargeValueError as e:
#     print(f"Помилка: {e}")
# except ValueError:
#     print("Помилка: Будь ласка, введіть ціле число.")