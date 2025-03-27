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
# --------------------------------- examples of dict comprehension
# Test data generating
user_ids = [101, 102, 103]
test_users = {uid: f"user_{uid}" for uid in user_ids}
# {101: 'user_101', 102: 'user_102', 103: 'user_103'}

statuses = {
    "payment1": "success",
    "payment2": "failed",
    "payment3": "success",
    "payment4": "pending"
}
successful = {k: v for k, v in statuses.items() if v == "success"}
# {'payment1': 'success', 'payment3': 'success'}

