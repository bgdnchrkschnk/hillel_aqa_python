from traceback import print_tb

sent = "My name is Bohdan"

# print(sent[11])
# print(sent.find('B'))
# print(sent.find('Boh'))
#
#
#
# # погане рішення
# bool_is_bohdan_in = bool(sent.find("Bof"))
# print(bool_is_bohdan_in)
# bool_is_My = bool(sent.find('M'), 0, -1)
# print("M", sent.find('M'))
#
# is_bohdan_in_str = False
# if sent.find('Bohdan') >= 0:
#     is_bohdan_in_str = True
#     print('Bohdan in the sentence')
#
# # альтернативний варіант
#

# if 'Byg' in sent:
#     print('Bohdan in the sentence')

# is_index = sent.find('is')
# len_word = len("is")
# #
# result_sent = sent[:is_index]  # розділити до слова is
# print('Cut before is:   ', result_sent)
# #
# result_sent = sent[is_index + len_word :]  # +2 бо is має довжину 2, поганий варіант
# print('Name:   ', result_sent)
#
#
sent = 'My name is Bohdan. Really is Bohdan'
print(sent.find("is", 10, -1))
search_word = 'name'
# print(sent.split("."))

# надрукувати все після слова search_word
search_word_index = sent.find(search_word)  # шукаю індекс початку цього слова(перша зустріч цього слова)
len_of_search_word = len(search_word)  # довжина слова після якого треба друкувати
final_index = search_word_index + len_of_search_word  # знаходжу індекс піля search_word
result_sent = sent[final_index:] # роблю слайс[search_word_index + len(search_word):]
print(result_sent)
