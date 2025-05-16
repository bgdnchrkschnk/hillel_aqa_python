def infinite_ids():
    i = 1
    while True:
        yield f"id_{i}"
        i += 1


def my_gen():
    for i in range(1_000_000):
        yield i


#  Можна використовувати у for, next(), any(), all(), zip(), sum(), list() — дуже гнучко.