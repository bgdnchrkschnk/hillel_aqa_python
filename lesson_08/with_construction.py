with open("custom_errors.py") as file:
    print(file.read())
#
# try:
#     file = open("custom_errors.py")
#     print(file.read())
# finally:
#     file.close()
# file = open("custom_errors.py")
# print(file.read())
# ...
# ...
# file.close()


import time
#
class Timer:
    def __enter__(self):
        self.start = time.time()
        print("🕒 Початок таймера")
        return self

    def __exit__(self, *args):
        duration = time.time() - self.start
        print(f"⏱ Виконано за {duration:.2f} сек")

# Використання
with Timer() as t:
    time.sleep(1.5) # чікування
    print("Щось довго рахуємо...")



# def my_func():
#     try:
#         ...
#     except Exception:
#         ...
#
# try:
#     my_func()
# except Exception:
#     ...

def my_func(list_elements: list):
    try:
        for element in list_elements:
            ...
    except TypeError:
        ...

my_func(list_elements=[1, 2, 3])

# ---------------------------------
def my_func(*args: int):
    try:
        for element in args:
            ...
    except TypeError:
        ...

my_func(*[1, 2, 3])

my_func(1, 2, 3, 4, 5)
