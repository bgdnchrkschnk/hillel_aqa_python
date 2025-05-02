from lesson_14.animal import Animal


class Dog(Animal):

    def __init__(self, name: str, color: str, bread: str, is_alive: bool = True):
        super().__init__(name, color, is_alive)
        self.bread = bread

    def speak(self):
        print(f"{self.name} says: GAV!")


