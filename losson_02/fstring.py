import datetime
#
# sofa_name: str = "Sofia"
# sofa_age: str = 18
# studied_years: int = 4
# # r - raw string, f - formatted string
# f_string = f"My name is {sofa_name} and my age is {sofa_age}. \nI am studying for {studied_years} years\n"
# print(f_string)
# sofa_age = 22
#
# print(f_string)



your_name: str = input("What is your name? ")
your_age: int = int(input("What is your age? ")) # "28"

f_string = f"Your data: Name - {your_name}, Age - {your_age}\nYou was born in {datetime.datetime.now().year - your_age}"
print(f_string)
