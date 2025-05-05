class Car:
    def __init__(self, model):
        self.model = model
        self.age = 1

    def ride(self):
        print("Riding....")

    def __del__(self):
        pass



# Initialization
my_car = Car("Toyota Camry")


# Utilization
my_car.ride()
my_car.age = 2


# Destruction
del my_car
my_car.age

#-------------------------------------------
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()
        print(f"File {self.filename} has been closed.")


# file = open("file.txt", "r")
# file.close()
#
# with open("file.txt", "w") as file:
#     file.write("")


# Використання об'єкта та автоматичний виклик деструктора
file_handler = FileHandler("example.txt", "r")
data = file_handler.read_data()
del file_handler

with open("example.txt", "w") as file:
    file.write(data)









