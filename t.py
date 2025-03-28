# # Given list of tuples (name, surname, age, profession, City location)
# # 1 - Add your new record o the beginning of the given list
# # 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# # 3 - check that all people in modified list with records indexes 6, 10, 13
# #   have age >=30. Print condition check result
#
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

people_records.insert(0, ('Lisa', 'Clark', 30, 'QA', 'Lviv'))

people_records[1], people_records[5] = people_records[5], people_records[1]

selected_indexes = [6, 10, 13]

age_check_6 = people_records[6][2] >= 30
age_check_10 = people_records[10][2] >= 30
age_check_13 = people_records[13][2] >= 30

is_over_30: bool = all([people_records[i][2] for i in selected_indexes]) # all([True, True, False])
list_records = []
for i in selected_indexes:
  if people_records[i][2] >= 30:
    list_records.append(people_records[i])
print(is_over_30)

print(f"person with index 6: {age_check_6}, person with index 10: {age_check_10}, person with index 13: {age_check_13}")


# all(iterable) all(list) all(tuple) all(set)

l = [{"id": 1,
      "age": 30},
     {"id": 2,
      "age": 40}]

ages = [record for record in l if record["age"] > 35]
print(ages)

print(all([record["age"] for record in l if record["age"] > 35])) # bool(element) - True

print(all([bool(element) is True, bool(element) is True]))