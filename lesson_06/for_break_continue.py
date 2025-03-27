
# список прав
users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': {'id': 1, 'title': 'QA'}},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': {'id': 2, 'title': 'CEO'}},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': {'id': 1, 'title': 'QA'}},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': {'id': 3, 'title': 'Retired'}},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': {'id': 1, 'title': 'QA'}},
]
#
# max_age = 40
# #
# for user in users:
#     if user['age'] <= max_age:
#         # some age actions
#         if len(user['name']) > 3:
#             if user.get('job') is not None:
#                 print(f'Hello, {user["name"]}')
#
# # -----------------------------------
# for user in users:
#
#     if user['age'] > max_age:  # old data, can't be validated
#         continue # пропускає дану ітерацію коли break обриває її
#     # some age actions
#
#     if len(user['name']) <=3:
#         continue
#     # some name actions
#
#     if user.get('job') is not None:
#         print(f'Hello, {user["name"]}')


transactions: list[dict] = db_client.get_all_transactions()

# for trx in transactions:
#     if trx["status"] == "failed":
#         print("Знайдено транзакцію зі статусом failed!")
#         break  # більше не шукаємо

for trx in transactions:
    if "merchant_id" not in trx:
        continue  # пропускаємо неповну транзакцію
    process_transaction(trx)

for index in range(10):
    print(index)
    if index == 8:
        break # обірвати цикл (вийти з цикла)
else:  # буде спрацьовувати якщо всередині циклу не відбувася break
    print('Done')


list_of_transactions = [{"id": 1,
                         "status": "failed"},
                        {"id": 2,
                         "status": "in_progress"},
                        {"id": 3,
                         "status": "success"},
                        {"id": 4,
                         "status": "failed"}
                        ]

for transaction in list_of_transactions:
    if transaction["status"] == "failed":
        print("Test failed!", transaction["id"])
        break


for number in range(11):
    if number % 2:
        continue
    print(number)

