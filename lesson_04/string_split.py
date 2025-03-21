# split ТІЛЬКИ для строк

sent = '"Would            yyou tell me, please, which way t much care where ——" said Alice'

# zero_case: list = sent.split('y')  # ['"Would  ', '', 'ou tell me, please, which wa', ' t much care where ——" said Alice']
# print(zero_case)
# first_split: list = sent.split(' ')  # ['"Would', '', 'yyou', 'tell', 'me,', 'please,', 'which', 'way', 't', 'much', 'care', 'where', '——"', 'said', 'Alice']
# print(first_split)
# second_case: list = sent.split()  #  ['"Would', 'yyou', 'tell', 'me,', 'please,', 'which', 'way', 't', 'much', 'care', 'where', '——"', 'said', 'Alice']
# # second_case = sent.split()  #  пробіл по замовчуванню
# print(second_case)


# index = 0
# for value in second_case:  # syntax: for ім'я_змінноЇ in список(або строка, або словник, або тапл, .. ітерабельний об'єкт)):
#     new_element = f'index is {index} is element: {value}'
#     print(new_element)
#     index += 1 # index = index +1




sent = '"Would you tell me, please, which way t much care where ——" said Alice'
my_phrases: list = sent.split(',')
print(my_phrases)
# ['"Would you tell me', ' please', ' which way t much care where ——" said Alice']
  # ctrl + /
print(f'first phrase = {my_phrases[0]}')
print(f'second phrase = {my_phrases[1]}')
print(f'third phrase = {my_phrases[2]}')


res = [
    '"Would you tell me',   # 0 index
    ' please',   # 1 index
    ' which way t much care where ——" said Alice'  # 2 index
]

# ctrl + /   закоментувати виділенне
# ctrl + d   продублюватит рядок
# ctrl + alt + l вирівняти код по PEP8 cmd + opt + l
# mac - command замість ctrl
#