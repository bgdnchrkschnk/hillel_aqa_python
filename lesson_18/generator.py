from lesson_06.for_cycle import counter


def get_names_generator(): # функція генератор
    yield "Bohdan"
    yield "Maksym"
    yield "Denys"
#
# generator_of_names = get_names_generator()
#
# first_name = next(generator_of_names)
# second_name = next(generator_of_names)
# third_name = next(generator_of_names)
#
#
# print(first_name, second_name, third_name)



# ------------------------------------------

# evens_numbers_generator = (i for i in range(10) if not i&2) # generator comprehension (скінчений)
#
# print(evens_numbers_generator)
#
# print(next(evens_numbers_generator))
# print(next(evens_numbers_generator))
# print(next(evens_numbers_generator))

# def generate_id_for_user():  # функція генератор (нескінчений)
#     id = 1
#     while True:
#         yield id
#         id += 1
#
# def second_type():
#     for i in range(100_000_000):
#         yield i
#
# generator_of_ids = generate_id_for_user()
#
# print(next(generator_of_ids))
# print(next(generator_of_ids))
# print(next(generator_of_ids))
# print(next(generator_of_ids))
#
#
# gen_two = second_type()
# print(next(gen_two))
# print(next(gen_two))
# print(next(gen_two))
#
#
# def count_up_to(limit): # функція генератор (скінчений)
#     count = 1
#     while count <= limit:
#         yield count
#         count += 1
#
# counter_up_to_30_generator = count_up_to(3)

# try:
#     print(next(counter_up_to_30_generator))
#     print(next(counter_up_to_30_generator))
#     print(next(counter_up_to_30_generator))
#     print(next(counter_up_to_30_generator))
#     print(next(counter_up_to_30_generator))
#     print(next(counter_up_to_30_generator))
# except StopIteration:
#     print("Generator stopped.")

# for k in counter_up_to_30_generator:
#     print(k)


# багато даних але не все одразу
def read_lines(file_path: str):
    with open(file_path) as f:
        for line in f:
            yield line


def generate_test_users():
    id = 1
    while True:
        yield {"username": f"user_{id}", "email": f"user_{id}@test.com"}
        id += 1

print(next(generate_test_users()))
