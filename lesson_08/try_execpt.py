# Приклад логічної помилки
def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"exception catched - {e}")
    except Exception as e:
        print(f"Unknown exception catched - {e}")
    else: # працює у випадку якщо ніяких помилок не виникло
        print("ELSE block")
        return result
    finally:
        print("finally block")


print(divide(10, "djbjkcbs"))
#
# list_: list = [10, 20, 30, None, 0]


# try:
#     db = session_db.connect(**config)
#     db.get_transactions()
# except ConnectionError as e:
#     print(f"Connection error: {e}")
# finally:
#     db.close()








# users = [
#     {'name': 'Den', 'math': 50, 'phil': 60},
#     {'name': 'Ivan', 'math': 50, 'phil': None},
#     {'name': 'Alex', 'math': 50, 'phil': 60},
#     {'name': 'Kim', 'phil': 45},
#     {'name': 'Illia', 'math': 50, 'phil': 60},
# ]
#
# def count_data(user_list: list):
#
#     for k in user_list:
#
#         try:
#
#             assert k['math'] + k['phil'] > 0  # код який виконати
#             print(k['name'], k['math'] + k['phil'] )
#
#         except KeyError as asd: # що перехоплювати
#
#             print(f'Cat get correct key {asd} for {k}')
#         #
#             # raise asd  # викликали помилку
#         #
#         except TypeError: # в бд можуть бути None
#
#             print(f'Found None, not a bug, continue')
#         #
#         # except Exception: # в бд можуть бути None
#         #
#         #     print(f'Unknown error')
#
#
# #
# # assert 1 == 1 # assert True = все ок
# # assert 1 == 2 #  assert False =>  AssertationError
#
#
#
# count_data(users)