class Rhombus:

    def __setattr__(self, key, value):
        if  key == "side_a" and value > 0:
            print(f"'{key}' key - has been assigned to the value of: '{value}'")
            super().__setattr__(key, value)
        elif key == "side_a" and value <= 0:
            print(f"'{key}' key- has been assigned to the value of: 'None'. '{key}' value should be > 0, please re-write this attribute!")
            super().__setattr__(key,None)
        elif key == "angle_a" and value <= 179:
            print(f"'{key}' key - has been assigned to the value of: '{value}'")
            super().__setattr__(key, value)
            second_angle = 180 - value
            setattr(self, "angle_b", second_angle)
            print(f"'angle_b' key - has been assigned to the value of: '{second_angle}'")
        elif key == "angle_a" and value > 179:
            print(f"'{key}' key- has been assigned to the value of: 'None'. '{key}' value should be <= 179, please re-write this attribute!")
            super().__setattr__(key,None)
        elif key == "angle_b":
            pass
        else:
            print(f"'{key}' key - has been assigned to the value of: '{value}'")
            super().__setattr__(key, value)


my_rhombus: Rhombus = Rhombus()
setattr(my_rhombus, "side_a", 10)
setattr(my_rhombus, "angle_a", 179)