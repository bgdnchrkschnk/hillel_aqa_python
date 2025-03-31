list_nums = range(0,11)

# list_evens: list[int] = list(
#     filter(lambda number: not number % 2, list_nums)
# )
#
# list_evens_quads: list[int] = list(
#     map(lambda number: number ** 4, list_nums)
# )
# print(list_evens)
# print(list_evens_quads)
#
#
# print_name_func = lambda name: print(name)
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