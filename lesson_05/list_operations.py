# списки

my_names = ['Nick', 'Alex']

print(id(my_names))
print(my_names)

my_names.append('Ivan')
print(id(my_names))
print(my_names)
#
# #
# print(my_names[0])
# print(my_names[1:])
# print(my_names[-1])
# print(my_names[::-1])
#
# # append, extend
# list_of_numbers = [1,2,3]
# my_names.append(list_of_numbers)
# print(my_names)
# my_names.extend(list_of_numbers) # [1,2,3] + [5,6,7]
# print(my_names)


# insert
# my_names = ['Nick', 'Alex', 'Ivan', 'Alex']
#
# my_names.insert(0, 'Viktor')
# print(my_names)
#
# #  pop
# my_names = ['Nick', 'Alex', 'Ivan', 'Alex']

# last_name = my_names.pop() # видаляє останній елемент і повертає його
# print(last_name)
# print(my_names)

# second_name = my_names.pop(2)  # by index, -1 by default
# print(second_name)
# print(my_names)

# remove
# my_names = ['Nick', 'Alex', 'Ivan', 'Alex']
# print(my_names)
# my_names.remove('Alex')  # by value
# print(my_names)
#
# text_with_names = ('I just want to add Dear Mr Here is the name Alex to all list of names because I did all names and '
#                    'I forgot to add ( Dear Mr )')
#
# list_with_text = text_with_names.split() # первтворення в список слів
#
# # пошук слів з великої літери
# list_of_names: list = []  # empty list
# for word in list_with_text:
#     print(f'check {word}: {word.istitle()}')
#     if word.istitle():
#         list_of_names.append(word)
#
# print(list_of_names)
#
# for word in list_of_names:
#     list_with_text.remove(word)
#
# print(' '.join(list_with_text))
#
# index
print(['A', 'B', 'B', 'C', 'C'].index('C')) #  індекс першого входження по значенню
#
# count
print([1,2,3,3,4].count(3))
print(['A', 'B', 'C', 'B', 'b'].count('B'))

new_list: list = [letter for letter in ['A', 'B', 'C', 'B', 'b'] if letter == "B" or letter == "b"]
print(new_list)
# print(len(set([1,2,3,3,4,5,4])))


