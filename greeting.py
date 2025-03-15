from datetime import date, datetime

print("HELLO WORLD")
greeting_version = 3.0
name = input("What is your name? ")


today = date.today()

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

two_days = today + datetime.timedelta(days=2)

three_days = today + datetime.timedelta(days=3)
