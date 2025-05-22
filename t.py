class Rhombus:
    def __init__(self, side_of_rhombus, angle_a):
        self.side_of_rhombus = side_of_rhombus
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_of_rhombus":
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Side length must be a positive integer")
        elif name == "angle_a":
            if not isinstance(value, int) or not (0 < value < 180):
                raise ValueError("Angle A must be between 1 and 179")
            super().__setattr__("angle_b", 180 - value)
        super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus: side = {self.side_of_rhombus}, angle A = {self.angle_a}, angle B = {self.angle_b}"

d = Rhombus(side_of_rhombus=20, angle_a=60)
print(d.angle_a)
print(d.side_of_rhombus)
print(d.angle_b)


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a  # angle_b is set automatically

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side length must be greater than 0.")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle A must be between 0 and 180 degrees.")
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("Angle B is automatically calculated from angle A.")

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus: side = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"


# d = Rhombus(20,60)
# print(d.angle_a)
# print(d.side_a)
# print(d.angle_b)