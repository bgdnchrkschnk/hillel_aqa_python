class LandTransport:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Land moving...")

    def horn(self):
        print("Horning like CAR...")

class WaterTransport:

    def __init__(self, model):
        self.brand = "TOYOTA"
        self.model = model

    def move(self):
        print("Water moving...")

    def horn(self):
        print("Horning like Boat...")

class AirTransport:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fly(self):
        print("flying...")

    def start_engine(self):
        print("Starting engine...")


class AmphibiousTransport(LandTransport, WaterTransport):

    def __init__(self, brand, model, amphibia_version):
        LandTransport.__init__(brand, model)
        WaterTransport.__init__(self, model) # only in first
        self.amphibia_version = amphibia_version
        print("Amphibious combines water and land transport.")


amphibious = AmphibiousTransport("Tesla", "AMPH-13", amphibia_version=1)
print(amphibious.brand)

# class FlyingBoatTransport(WaterTransport, AirTransport):
#
#     def __init__(self, brand, model):
#         WaterTransport.__init__(self, brand, model)
#         AirTransport.__init__(self, brand, model)
#
#     def horn(self):
#         print("Horning like Flying Boat...")

# class HybridTransport(AmphibiousTransport, FlyingBoatTransport):
#     def __init__(self, brand, model):
#         AmphibiousTransport.__init__(self, brand, model)
#         FlyingBoatTransport.__init__(self, brand, model)
#
#     def description(self):
#         print("Hybrid transport. i can everithing")