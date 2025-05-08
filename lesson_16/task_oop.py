"""Опишіть об’єкт «Поїзд». Клас повинен містити поля та метод для додавання вагонів
(необхідно додати об’єкти та екземпляри класу вагонів).

В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
Опишіть клас Вагон разом із поїздом. Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
У Вагоні може бути не більше 10 пасажирів.
"""

class Wagon:
    def __init__(self, number, is_locomotive=False):
        self.number = number
        self.list_of_passengers: list = []
        self.is_locomotive: bool = is_locomotive


    def add_passenger(self, passengers: str | list[str]) -> None:
        if len(self.list_of_passengers) >= 10:
            return
        if self.is_locomotive:
            return
        if isinstance(passengers, str):
            self.list_of_passengers.append(passengers)
        elif isinstance(passengers, list):
            if len(self.list_of_passengers.copy() + passengers) <= 10:
                self.list_of_passengers.extend(passengers)

    def __repr__(self) -> str:
        return f"Wagon number {self.number}. Is_locomotive: {self.is_locomotive}. Passengers: {self.list_of_passengers}"


class Train:
    def __init__(self):
        self.locomotive: Wagon = Wagon(is_locomotive=True, number=1)
        self.list_of_wagons: list[Wagon] = []
        self.add_wagon(self.locomotive)

    def add_wagon(self, wagon: Wagon):
        self.list_of_wagons.append(wagon)

train: Train = Train()
wagon_two : Wagon = Wagon(number=2)
wagon_two.add_passenger(["Diana", "Kostya", "Oleksandr", "Bohdan"])
print(wagon_two.list_of_passengers)
train.add_wagon(wagon_two)



print(train.list_of_wagons)
