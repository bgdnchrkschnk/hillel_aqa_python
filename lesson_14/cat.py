from lesson_14.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, color: str, bread: str, is_alive: bool = True):
        super().__init__(name, color, is_alive)
        self.bread = bread

    def speak(self):
        print(f"{self.name} says: MEOW!")

    def cat_biography(self):
        return f"Hello, I am cat. My name is {self.name} - {self.bread} bread. My color is {self.color}. I am {self.is_alive} alive."









