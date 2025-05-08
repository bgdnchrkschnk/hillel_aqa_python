# class Guitarist:
#     def perform(self):
#         print("Playing a guitar")
#
# class Singer:
#     def perform(self):
#         print("Singing...")
#
# class Artist(Singer, Guitarist):
#     def perform(self):
#         print("Playing a guitar and singing..!")



# artist = Artist()
# artist.perform()
#
# print(Artist.mro())

# ------------------------------------
# class Human:
#     def perform(self):
#         print("Moving to a scene")
#
# class Guitarist(Human):
#     def perform(self):
#         super().perform()
#         print("Playing a guitar")
#
# class Singer(Human):
#     def perform(self):
#         super().perform()
#         print("Singing...")
#
# class Artist(Singer, Guitarist):
#     def perform(self):
#         Singer.perform(self)
#
# art = Artist()
# art.perform()

# ---------------------------------------

class LandTransport:
    def move(self):
        print("Land moving...")

    def horn(self):
        print("Horning like CAR...")

class WaterTransport:
    def move(self):
        print("Water moving...")

    def horn(self):
        print("Horning like Boat...")

class AirTransport:
    def fly(self):
        print("flying...")

    def start_engine(self):
        print("Starting engine...")

class AmphibiousTransport(WaterTransport, LandTransport):
    pass

class FlyingBoatTransport(WaterTransport, AirTransport):
    def horn(self):
        print("Horning like Flying Boat...")

class HybridTransport(AmphibiousTransport, FlyingBoatTransport):
    def description(self):
        print("Hybrid transport. i can everithing")


hybrid_transport = HybridTransport()
hybrid_transport.move()
hybrid_transport.fly()
hybrid_transport.start_engine()
hybrid_transport.horn()

print(HybridTransport.mro())