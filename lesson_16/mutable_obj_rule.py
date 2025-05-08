class Person:
    def __init__(self, name, friends=None):
        self.name = name
        self.friends = [] if not friends else friends


bogdan = Person(name="Bohdan")
print(bogdan.friends)

bogdan.friends.append("Kostya")
print(bogdan.friends)

den = Person(name="Den")
print(den.friends)