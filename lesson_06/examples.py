# person = ('Den', 25, 'AQA')
#
# people = [
#     ('Den', 26, 'AQA'),
#     ('Den', 25, 'AQA'),
# ]
#
# for p in people:
#     p[0]  # name
#     p[1]  # age
#
#     if person_name == p[0]:
#         pass


# isinstance - для дз задача 3

#
# name = "Nikita"
#
# if name == "Bohdan":
#     print(f"Hello, {name}")
# elif name == "Nikita":
#     print(f"Hello, {name}, I waited for you!")
# else:
#     print(f"Hello, {name}. I didn't see you yet.")
#
# set_of_statuses: set = {"approved", "in_progress", "done"} # "approve", "in_progress", "done"
#
# for statuse in set_of_statuses:
#     print(statuse)
#     if statuse == "done":
#         break
# else: # це спрацьовує якщо цикл повністю завершився, не був обірваний
#     print("Else")
#
# number = 0
# while number < 10: # while <вираз або булеве значення>
#     number += 1
#     print(number)
# print("Else")
#
#
# set_of_statuses: set = {"approved", "in_progress", "done"} # "approve", "in_progress", "done"
#
# for statuse in set_of_statuses:
#     if statuse == "in_progress":
#         continue
#     print(statuse)
# else: # це спрацьовує якщо цикл повністю завершився, не був обірваний
#     print("Else")
#
#
#
# string: str = input("Enter a string: ")
#
# for letter in string:
#     print(letter)

string = "Weather" #
if "ther" in string:# list(string):
    print("YES")
else:
    print("no")

list_of_data = [1, 2, 3.0, True, {}, "hello"]

for item in list_of_data:
    print(type(item))
    print(type(item) == int)
    print(isinstance(item, int))



