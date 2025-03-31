# all - всі елементи - True
print(all(["sjhjuf", True, 88, [1,2]]))

# any - хочаб один елемет - True
print(any([12, 0, "string"]))

#ascii
ascii_ukraine = ascii("Україна") # "'\\\\u0423\\\\u043a\\\\u0440\\\\u0430\\\\u0457\\\\u043d\\\\u0430'"
print(ascii_ukraine)
print('\u0423\u043a\u0440\u0430\u0457\u043d\u0430')


# callable
name: str = "Bohdan"

def print_my_name():
    print("Bohdan")

print(
    callable(print_my_name)
)

# chr
print(chr(100))

# for i in range(1000):
#     print(chr(i))

# ord
print(ord("d"))


# compile
code = '''
def greet(name):
    print("Hello, " + name)

greet("World")
'''
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)


expression = '2 + 3 * 4'
compiled_expression = compile(expression, '<string>', 'eval')
result = eval(compiled_expression)
print(result)

# dict
my_dict = {"name": "Bohdan",
           "age": 28}

my_dict_2 = dict(**my_dict, school="Hillel")

# enumerate

my_list: list = ["referf","ehghv", "hth"]

my_dict = {"name": "Bohdan",
           "age": 28}

for index, item in enumerate(my_list):
    print(index, item)


# filter
list_of_nums: list[int] = list(range(11))

def num_is_even(num):
    return num % 2 == 0

list_2_evens: list[int] = list(filter(num_is_even, list_of_nums))
print(list_2_evens)
list_2_without_7: list[int] = list(filter(lambda num: num!= 7, list_of_nums))
list_2_without_7_lc: list[int] = [number for number in list_of_nums if number != 7]


list_of_nums: list[int] = list(range(11))
list_of_nums.append("None")
print(list_of_nums)

new_list_filtered: list[int] = list(filter(
    lambda element: isinstance(element, int), list_of_nums
))
list_2_filtered_lc: list[int] = [number for number in list_of_nums if isinstance(number, int)]

print(list_2_filtered_lc)


# map
list_of_names: list[str] = ["bohdan", "denys", "mykola", "diana"]

list_of_names_2: list[str] = list(
    map(str.title, list_of_names)
)


list_of_names_3: list[str] = list(
    map(lambda el: el+"2025", list_of_names)
)
list_of_names_4_lc: list[str] = [name+"2025" for name in list_of_names]

print(list_of_names_4_lc)


list_of_transactions: list[dict] = [{"id": 1,
                                     "tran_type": "purchase",
                                     "status": "success",
                                     "extra_info": {}},
                                    {"id": 2,
                                     "tran_type": "purchase",
                                     "status": "failed",
                                     "extra_info": {"merchant_id": 20,
                                                    "company_name": "Hillel"}},
                                     {"id": 3,
                                      "tran_type": "reverse",
                                      "status": "success",
                                      "extra_info": {}},
                                    {"id": 4,
                                     "tran_type": "purchase",
                                     "status": "failed",
                                     "extra_info": {"merchant_id": 25,
                                                    "company_name": "Kyivstar"}}]


def is_failed_hillel(transactions_data: dict):
    if transactions_data["status"] == "failed":
        extra_info = transactions_data.get("extra_info")
        if extra_info:
            if extra_info.get("company_name") == "Hillel":
                return True


list_filered: list[dict] = list(
    filter(is_failed_hillel, list_of_transactions)
)
print(list_filered)


# zip

list1 = [1, 2, 3, 10, 11]
list2 = ['a', 'b', 'c']
# list3 = ["one", "two", "three", "four", "five"]
zipped = zip(list1, list2)
print(tuple(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c')]


# isinstance/type

a: int = 100
b: bool = True

class Int_2(int):
    pass

# int -> int_son


# a_new = Int_2()

# if type(a_new) == Int_2:
#     print(a, "is INT_2")
#
# if isinstance(a_new, int):
#     print(a_new, "is integer")

# print(isinstance(1, object))


functions_make_upper = lambda element: element.upper()

sum_two_numbers = lambda first_number, second_number: first_number + second_number

print(functions_make_upper("nikita"))

print(sum_two_numbers(first_number=110, second_number=-20.7))