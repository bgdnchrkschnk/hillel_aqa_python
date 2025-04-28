import csv

# Дані для запису у CSV-файл
data = [
    ['Name', 'Age', '', 'Bool'],
    ['John', 30, 'New York', False],
    ['Alice', 25, 'Los Angeles', None],
    ['Bob', None, 'Chicago', True]
]


# Відкриття CSV-файлу для запису
with open('output.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(data)


with open('files/output.csv', 'r', newline='') as csvfile:
    # reader = tuple(csv.reader(csvfile)) # generator -> iterable
    reader = csv.reader(csvfile)
    for row in reader: # generator_object - reader
        print(row)




    # header = reader[0]
    # data = reader[1:]
    # print(header)
    # print(data)

    # for row in reader: # generator_object - reader
    #     print(row)


# with open('files/output.csv', 'r') as csv_file:
#
#     reader = list(csv.reader(csv_file))
#
#     header = reader[0]
#     row_data = reader[1:]
#
#     print('Header is:', header)
#     for index, row in enumerate(row_data, start=1):  # enumerate index, row
#         print(f'{index} row is :', row)
