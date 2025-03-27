from rich import status

set_comprehension: set = {v for v in range(11)} # {element}
print(set_comprehension)

list_comprehension: list = [v for v in range(11)] # [element]
print(list_comprehension)
range_obj = range(11)
print(range_obj)
for obj in range_obj:
    print(obj)

# my_dict = {"key": "value"}
# name = "Bohdan"
# dict_comprehension: dict = {index+10: name.upper() for index in range(11)} # {key: value }
# print(dict_comprehension)
# --------------------------------- examples of dict comprehension
# Test data generating
user_ids = [101, 102, 103, 104, 105, 106, 107, 108, 109]
test_users = {uid: f"test_user_{uid}" for uid in user_ids}
# {101: 'user_101', 102: 'user_102', 103: 'user_103'}
print(test_users)

# for status in statuses.keys(): # по ключам
#     print(status)

# for value in statuses.values():  # по ключам
#     print(value)
#
# for key, value in statuses.items(): # ключ+значення
#     print(key, value)
statuses = {
    "payment1": "success",
    "payment2": "failed",
    "payment3": "success",
    "payment4": "pending"
}

successful_payments: dict = {key: value for key, value in statuses.items() if value == "success"} # [("payment1", "success"), ("payment2", "failed")...]
# successful = {k: v for k, v in statuses.items() if v == "success"}
# {'payment1': 'success', 'payment3': 'success'}

print(successful_payments)
