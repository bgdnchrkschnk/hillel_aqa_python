# my_name = 'BoHDan CheRKaScHENkO is hillel LectoR'
# print(my_name)
# my_name = my_name.upper()
# # print(my_name.upper())  # в верхній регістр кожне слово
# # print(my_name.lower())  # в нижній  регістр кожне слово
# # print(my_name.title())  # З великої кожне слово(розділення по будь-якому символу НЕ буква)
# # print(my_name.capitalize())  # першу дуве зробить великою, інші малі
# print(my_name)
#
my_name = 'Bohdan Cherkschenko'
is_upper: bool = my_name.isupper()
print(is_upper)
print(my_name.islower())
print(my_name.istitle())
print(my_name.swapcase())

# answer = 'asd UsD' # "usd USD Usd"
# # answer = answer.lower()
# to_find = ["Usd", "USD", "usd"]
# for find in to_find:
#     if find in answer:  # answer.lower() = переводить все в answer в нижній регістр
#         print('True')