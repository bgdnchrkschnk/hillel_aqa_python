list_nums = range(0,11)

list_evens: list[int] = list(
    filter(lambda number: number % 2, list_nums)
)

def num_is_mot_even(number):
    if number % 2 == 0:
        return True

#
list_evens_quads: list[int] = list(
    map(lambda number: number*2, list_nums)
)

def num_twice(number):
    return number * 2
# print(list_evens)
# print(list_evens_quads)
#
#

def some_function(name):
    ...
    print(name)


some_function_lambda = lambda name, age: print(name) if age==18 else None

some_function_lambda(name="Bohdan", age=18)

#
# print_name_func(name="Bohdan")
#
# list_of_names: list[str] = ["Bohdan", "Mykola", "Kyrylo", "Borys"]
#
# list_of_names_bo: list[str] = list(
#     filter(lambda name: name.startswith("Bo"), list_of_names)
# )
# list_of_names_bo_map: list[str] = list(
#     map(lambda name: name if name.startswith("Bo") else None, list_of_names)
# )
#
# list_of_names_bo_comprehention: list[str] = [name for name in list_of_names if name.startswith("Bo")]
#
#
# print(list_of_names_bo)
# print(list_of_names_bo_map)
# print(list_of_names_bo_comprehention)