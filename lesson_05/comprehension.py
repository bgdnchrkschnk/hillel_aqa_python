set_comprehension: set = {v for v in range(11)} # {element}
print(set_comprehension)

list_comprehension: list = [v for v in range(11)] # [element]
print(list_comprehension)
range_obj = range(11)
print(range_obj)
for obj in range_obj:
    print(obj)

dict_comprehension: dict = {index: index**2 for index in range(11)} # {key: value }
print(dict_comprehension)