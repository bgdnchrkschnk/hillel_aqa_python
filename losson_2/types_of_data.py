# Незмінні (Immutable)
int_var: int = 42 # int
float_var: float = 3.14              # float
bool_var: bool = True               # bool
str_var: str = "Hello, Python!"    # str
# 0, 1, 2, 3
tuple_var: tuple = ("Monday", "Tuesday", "Wednesday")         # tuple
frozenset_var = frozenset({1, 2, 3})  # frozenset

# Змінні (Mutable)
list_var: list = [1, 1, 3.2, True, [1,2,3], {}]          # list
set_var: set = {1, 2, 3}           # set
dict_var: dict = {"key": "value"}   # dict

splited_str: list = str_var.split(",")
for some_value in splited_str:
    print(some_value)

# print(str_var[-1])
# print(tuple_var[-1])
# print(list_var[1])
# print("my list element is:", list_var[4])
#
# # element[start:end:step]
# print(str_var[0:2])
# print(str_var[1:7])
# print(str_var[0:-1:2])
# print(list_var[::-1])
#
# print(len(str_var))
# print(len(list_var))

my_bio: dict = {"name": "Bohdan",
          "age": 28,
          "friends": ["Kolya","Denys"],
          }
#
# print(my_bio["friends"])
# print(my_bio["age"])
# print(my_bio["friends"][1])

# for item in my_bio.items():
#     print(item)

incoming_salary: float = None
account_number: str = None
print(not incoming_salary)


l: list[int | str] = [1, 55, 8]

