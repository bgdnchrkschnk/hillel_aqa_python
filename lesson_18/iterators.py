# Створення ітератора для списку
my_iterable = iter([1, 2, 3, 4, 5])

# Прохід по ітератору вручну
# print(next(my_iterable))  # Виведе: 1
# print(next(my_iterable))  # Виведе: 2
# print(next(my_iterable))  # Виведе: 3
# print(next(my_iterable))  # Виведе: 4
# print(next(my_iterable))  # Виведе: 5
# # print(next(my_iterable))
#
# # Помилка StopIteration при спробі отримати наступний елемент
# try:
#     print(next(my_iterable))
# except StopIteration:
#     print("StopIteration: Ітератор закінчився")

# ------------------
# for value in my_iterable:
#     print(value)


# -------------------
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Використання власного ітератора
my_iterator = MyIterator(limit=5)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))



list_of_transactions_ids: list[int] = [111, 129, 247, 50]

iterator_of_transactions_ids = iter(list_of_transactions_ids)

print(next(iterator_of_transactions_ids))