from lesson_14.animal import Animal


class Pig(Animal):
    def __init__(self, name: str, color: str, weight: str, is_alive: bool = True):
        super().__init__(name, color, is_alive)
        self.weight = weight

    def speak(self):
        print(f"{self.name} says: HRYU!")

