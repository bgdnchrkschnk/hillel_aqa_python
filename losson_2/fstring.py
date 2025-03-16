import datetime

sofa_name: str = "Sofia"
sofa_age: str = 18
studied_years: int = 4

f_string = f"My name is {sofa_name} and my age is {sofa_age}. I am studying for {studied_years + 1} years\n"

sofa_age = 22

print(f_string)



your_name: str = input("What is your name? ")
your_age: int = input("What is your age? ")

f_string = f"Your data: Name - {your_name}, Age - {your_age}\nYou was born in {datetime.datetime.now().year - your_age}"
print(f_string)
