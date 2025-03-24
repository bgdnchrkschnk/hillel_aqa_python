# списки
from traceback import print_tb
#
# my_names = ['DDena', 'DVaenaa','Alex', 'Viktor', 'Xena']
# my_ages = [1,2,3,1,2,3]
#
# sorted_names = sorted(my_names, reverse=False)  # by default  reverse=False
# sorted_ages = sorted(my_ages)  # by default  reverse=False
# print(sorted_ages)
# print(sorted_names)
#
# sorted_names_reverse = sorted(my_names, reverse=True)
# sorted_ages_reverse = sorted(my_ages, reverse=True)
# print(sorted_names_reverse)
# print(sorted_ages_reverse)
#
# # print(sorted_names)
# # print(my_names)
# # print(sorted_names_reverse)
# # print(sorted_ages)
# # print(sorted_ages_reverse)
#
#
# # змінює оригінальний список коли sorted - створює новий
# print(sorted((1,5,3,4)))
# my_list_of_items = ['Den', 'Alex', 'Viktor']
# print(id(my_list_of_items))
# my_list_of_items.sort(reverse=True)
# print(my_list_of_items)
# print(id(my_list_of_items))
# new_list = sorted(my_list_of_items)
# print(sorted(my_list_of_items))  # error
#
# print(my_names)
# my_names.sort(reverse=True)
# print(my_names)
# my_names.sort(reverse=False)
# print(my_names)
#
# sorted_tuple = sorted((1,3,4,2))
# print(sorted_tuple)

# ---------------------------
# my_names = ['DDena', 'DVaenaa','Alex', 'Viktor', 'Xena']
# sorted_names_by_default = sorted(my_names)
# sorted_names_by_len = sorted(my_names, key=lambda list_element: len(list_element))
# print(sorted_names_by_len)
#
# # lambda x: len(x) - анонімна функція, лямбда функція
#
# # іншими словами
# def calculate_len_of_list_element(list_element):
#     result = len(list_element)
#     return result
#
# sorted_names_by_len_custom = sorted(my_names, key=calculate_len_of_list_element)
# print(sorted_names_by_len_custom)
#  => sorted([len('DDena'), len('DVaenaa'), len('Alex'), len('Viktor'), len('Xena')])
#  => sorted([calculate_len_of_list_element('DDena'), calculate_len_of_list_element('DVaenaa'), calculate_len_of_list_element('Alex'), calculate_len_of_list_element('Viktor'), calculate_len_of_list_element('Xena')])
#
# print(sorted_names_by_default)
# print(sorted_names_by_len_custom)
# print(sorted_names_by_len)