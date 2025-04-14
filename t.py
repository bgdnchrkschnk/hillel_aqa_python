# # task 1
# """ Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.
# """
# def multiplication_table(number: int) -> None:
#     multiplier: int = 1
#     result: int = 0
#     max_summa: int = 25
#
#     while result <= max_summa:
#         result = number * multiplier
#         if  result > 25:
#             break
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#
#         multiplier += 1
#
# multiplication_table(3)
# # Should print:
# # 3x1=3
# # 3x2=6
# # 3x3=9
# # 3x4=12
# # 3x5=15
#
#
# # task 2
# """  Написати функцію, яка обчислює суму двох чисел.
# """
# def summa_values(value_a: int,value_b: int) -> int:
#     return value_a + value_b
#
# print("Сума значень:", summa_values(2,3))
#
# # task 3
# """  Написати функцію, яка розрахує середнє арифметичне списку чисел.
# """
# def arithmetic_mean_list(*args) -> float:
#     count_value_in_list: int = len(args)
#     summa_arg: int = 0
#     for arg in args:
#         summa_arg += arg
#     arithmetic_mean = summa_arg / count_value_in_list
#     return arithmetic_mean
#
# list_value: list[int] = [1,3,5,12]
# print("Cереднє арифметичне списку чисел:",arithmetic_mean_list(*list_value))
#
# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# """
#
# def string_in_reverse(text: str) -> str:
#     text_reverse: str = text[::-1]
#     return text_reverse
#
# text_input: str = "Написати функцію, яка приймає рядок"
# print(string_in_reverse(text_input))
#
# # task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
# """
# def longest_word(*args) -> str:
#     len_arg_max_word: str = args[0]
#     for arg in args:
#         if len(arg) > len(len_arg_max_word):
#             len_arg_max_word = arg
#     return len_arg_max_word
#
# word_list: list[str] = ["функція","яка","прийматиме","список","слів"]
# print("Найдовше слово у списку:", longest_word(*word_list))
#
# # task 6
# """  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""
# def find_substring(str1, str2) ->int:
#     if str2 in str1:
#         index_str2_in_str1 = str1.find(str2)
#         return index_str2_in_str1
#     else:
#         return -1
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1
#
# # task 7
# """Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()"""
#
# def number_of_unique_characters(*args) -> bool:
#     if len(set(input_symbol)) > 10:
#         return True
#     else:
#         return False
#
# input_symbol: str = input("Введіть будь який текст: ")
# print(number_of_unique_characters(input_symbol))
#
# # task 8
# """Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""
#
# def summa_even_value(*args) -> int:
#     sum_even_value: int = 0
#
#     for numbers in lst1:
#         if numbers % 2 == 0:
#             sum_even_value += numbers
#     return sum_even_value
#
# lst1: list = [1,5,9,2,18,103,10]
# print(summa_even_value(lst1))

# task 9
"""Exists some car data with color, year, engine_volume, car type , price
We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
write code that will help us to get cars that satisfy search_criteria.
"""
def car_data_search_criteria(table: dict, criteria: tuple) -> None:
    car_search_criteria: dict = {}

    for key, value in table.items():
        if value[1] >= criteria[0] and value[2] >= criteria[1] and value[4] <= criteria[2]:
            car_search_criteria[key] = value
    sorted_car_data_search_criteria: list = sorted(car_search_criteria.items(), key=lambda x: x[1][4])
    print("Car search criteria:\n", sorted_car_data_search_criteria[:5])

car_data: dict = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

search_criteria: tuple = (2017, 1.6, 26000)
car_data_search_criteria(table = car_data, criteria = search_criteria)

# # task 10
#
# adwentures_of_tom_sawer: str = """\
# Tom gave up the brush with reluctance in his .... face but alacrity
# in his heart. And while
# the late steamer
# "Big Missouri" worked ....
# and sweated
# in the sun,
# the retired artist sat on a barrel in the .... shade close by, dangled his legs,
# munched his apple, and planned the slaughter of more innocents.
# There was no lack of material;
# boys happened along every little while;
# they came to jeer, but .... remained to whitewash. ....
# By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
# a kite, in good repair;
# and when he played
# out, Johnny Miller bought
# in for a dead rat and a string to swing it with—and so on, and so on,
# hour after hour. And when the middle of the afternoon came, from being a
# poor poverty, stricken boy in the .... morning, Tom was literally
# rolling in wealth."""
#
# """ Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
#
# def replacing_hyphenation_in_sentence(text: str) -> str:
#     replace_sentence_in_text: str = text.replace("\n", " ")
#     return replace_sentence_in_text
#
# print(replacing_hyphenation_in_sentence(adwentures_of_tom_sawer))