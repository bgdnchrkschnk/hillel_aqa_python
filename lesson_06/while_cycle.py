import random  # бібліотека для випадкових значень



# while bool or condition
#
counter = 0
while True:  # вічний цикл
    counter += 1
    if counter == 6:
        continue
    if counter == 10:
        break
    print(counter)



# ----------------
counter = 0
expected = 5

while counter < expected:
    print(f"Counter: {counter}")
    counter += 1
print("Expected number is reached!")

tasks = ["login", "pay", "refund", "logout"]

# for task in tasks:
#     print("Doing", task)
#
# while bool(tasks):
#     current_task = tasks.pop(0)
#     print(f"Task in process: {current_task}")
# print("All tasks done!")
# attemps = 0
# max_attempts = 5
# while attempt < max_attempts:
#     status = api.get_payment_status(order_id)
#     if status == "success":
#         break
#     elif status == "failed":
#         pytest.fail("Платіж завершився з помилкою")
#     else:
#         time.sleep(2)
#         attempt += 1
# else:
#     pytest.fail("Статус платежу не змінився на success вчасно")
#
#
# timeout = 10  # секунд
# attempts = 0
#
# while elapsed < timeout:
#     result = db_client.get_transaction_by_id(tran_id)
#     if result:
#         print("Транзакція з'явилася в базі")
#         break
#     time.sleep(1)
#     attempts += 1
# else:
#     pytest.fail("Транзакція не з'явилась у базі за очікуваний час")
#


