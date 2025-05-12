class Diamond:

    def __init__(self, side_a, angle_a):
        self.side_a: int|float = side_a
        self.angle_a: int|float = angle_a
        self._angle_b: int|float = self.__calc_adjacent_angle(angle_a)

    def __calc_adjacent_angle(self, angle_a):
        return 180 - angle_a

    def __setattr__(self, key, value):
        if value <= 0:
            raise ValueError(f'{value} is not valid for {key}')
        if key == "angle_a" and  value >=180:
            raise ValueError(f'{value} is not valid for {key} in Diamond.'
                             f' Must be less tnah 180 for Diamond')
        print(f"\nSetting {key} to {value}")
        super().__setattr__(key, value)
        if key == "angle_a":
            new_b = self.__calc_adjacent_angle(value)
            super().__setattr__("_angle_b", new_b)

    def __str__(self):
        return f"Diamond(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self._angle_b})"


diamand_1: Diamond = Diamond(3, 70)
print(diamand_1)

diamand_1.side_a = 4
print(diamand_1)

diamand_1.angle_a = 130
print(diamand_1)