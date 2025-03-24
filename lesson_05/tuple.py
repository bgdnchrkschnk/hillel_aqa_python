# # кортеж
#
# my_names = ('Den', 'Alex', 'Viktor') # () - tuple, [] - list
#
#
# print(my_names)
# print(my_names[0:2])
# print('-'*80)
#
# for name in my_names:
#     print(name)
# print('-'*80)
# print(my_names[1:])
# #
#
# my_names = ('Den', 'Alex', 'Viktor')
# my_name, alex_name, friend_name = ('Den', 'Alex', 'Viktor')
# print(my_name)
# print('-'*80)
# print(my_names)
# print(*("Monday", "Tuesday", "Wednesday"))
# print(*my_names) # ==>
# print('Monday', 'Tuesday', 'Wednesday')
# print('Den', 'Alex', 'Viktor')
# print('-'*80)
# # ------------------------------
# my_name, *not_my_names, last_name = ('Den', 'Alex', 'Viktor', 'Ivan', 'Serge')
# print(my_name)
# print(not_my_names)
# print(last_name)
# # ------------------------------
# # приведення до tuple
# some_text = 'bla-bla'
#
# tuple_text = tuple(some_text)  # ('b', 'l', 'a', '-', 'b', 'l', 'a')
# print(type(tuple_text))
#
# my_list = [1,2,3]
# new_tuple_from_list = tuple(my_list)
# print(new_tuple_from_list)

# ------------------------------

# my_list = [1,2]
#
# my_tuple_with_evr = (1, my_list, 'asd', None, (1,2), {"one": 1, "two": 2}, "new_element")  # це tuple
# print(my_tuple_with_evr)
#
# my_list.append([None, True])
# my_tuple_with_evr[-1]["new_value"] = 12
# print(my_tuple_with_evr)


# empty_tuple: tuple = ()
# empty_list: list = []
# print(bool(empty_tuple))
# print(bool(empty_list))
#
# print(empty_tuple)
# empty_tuple_2 = tuple()
#
# print(type(empty_tuple))
# print(type(empty_tuple_2))
#
# tuple_with_1_el = (42,)
# not_tuple_with_1_el = (42)
# print(type(tuple_with_1_el))
# print(type(not_tuple_with_1_el))
#
#
#
#
#
# t: tuple = (1, 2, 3, 4)
# first, *x, last = t
# print(x)
# a, b, c, d = t
#
#
# print(*t)
# print(a,b,c,d)

# transactions_from_api: list = []
# transactions_from_api.append(1123)