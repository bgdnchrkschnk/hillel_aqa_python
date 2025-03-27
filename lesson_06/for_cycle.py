names = ['Den', 'Alex', 'Georg']
ages = [10, 20, 30]

name = 'Den'

for name in names:
    print(name)

#
name = names[0]
print(name)
name = names[1]
print(name)
name = names[2]
print(name)  # Georg

#
# test_amounts = [100, 500, 1000]
#
# for amount in test_amounts:
#     response = make_payment(amount=amount)
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"

# currencies = ["GEL", "USD", "EUR"]
# amounts = [100, 500, 1000]
#
# for currency in currencies:
#     for amount in amounts:
#         response = api_client.send_payment({"currency": currency, "amount": amount})
#         assert response.status_code == 200

# names = ['Den', 'Alex', 'Georg']
# ages = [10, 20, 30]
#
# for k in names:
#     print(k)
#
#     for n in ages:
#         print(n)
#
#
# for _ in range(10):
#     print('Hello')
