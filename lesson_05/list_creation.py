my_list_1 = [1, 2, 3, 'Alex', [1, 0, False, [55, "Olena"]], None, ()]

print(my_list_1[-3][-1][1])

my_list_2 = list('Alex, Ivan, Den')

my_tuple = (1,2,3,4)

my_list_3 = list(my_tuple) # tuple to list, list to tuple

print(my_list_1)
print(my_list_1[0]) # 1
print(my_list_1[-1]) # None

print(my_list_2)
print(my_list_2[0]) # A
print(my_list_2[-1]) # n

print(my_list_3)
print(my_list_3[0]) # 1
print(my_list_3[-1]) # 4

# помилка
# list(False)
# list(5)
# list(None)
# print(list(1,2)) # list(iterable) , tuple(iterable)
# print(tuple([1,2,3,4,5]))


my_numbers = [1,2,3,4,5]

my_numbers_filtered = [number for number in my_numbers if number % 2 == 0]
print(my_numbers)
print(my_numbers_filtered)


# свторити список з квадратими ци х чисел

sq_list = []
for number in my_numbers:
    if number % 2 == 1:  #  якщо непарне
        sq_list.append(number ** 2)


print(sq_list)

sq_list_lc = [asdasd ** 2 for asdasd in my_numbers if asdasd % 2 == 1]  # List comprehension
square_list: list = [number ** 2 for number in my_numbers if number % 2 == 1]
string = "Hello World!5"
new_list = [element for element in string if element.isdigit()]
print(new_list)
print(square_list)




print(sq_list_lc)

range

my_range_0_to_9 = range(10)  # 0 .. 9
print(list(my_range_0_to_9))

my_range_10_to_14 = range(10, 15)  # 10 .. 14
print(list(my_range_10_to_14))

my_range_20_to_38 = range(20, 40, 2)  # 20, 22, ... 38 не включаючі 40
print(list(my_range_20_to_38))

my_range_40_to_22 = range(40, 20, -2)  # 40, 38, ... 22 не включаючі 20
print(list(my_range_40_to_22))


sq_list_100 = [k**2 for k in range(1, 101)]
print(sq_list_100)

range_numbers = range(1,100)
print(type(range_numbers), range_numbers)