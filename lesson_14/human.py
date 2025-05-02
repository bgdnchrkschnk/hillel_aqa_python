class Human:

    head = 1
    hands = 2
    need_eat: bool = True

    def __init__(self, name, age, sex, is_bold: bool = False):
        self.name = name
        self.age = age
        self.sex = sex
        self.is_bold: bool = is_bold
        self.is_adult = True if self.age >= 18 else False



human_one = Human('Mykyta', 18, 'male')
print(human_one.is_adult)
