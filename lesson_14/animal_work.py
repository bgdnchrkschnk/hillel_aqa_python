from lesson_14.animal import Animal
from lesson_14.cat import Cat
from lesson_14.dog import Dog
from lesson_14.pig import Pig



barsik: Dog = Dog(name="barsik", color="white", bread="boxer")
sharik: Cat = Cat(name="sharik", color="red", bread="siam")
molly: Pig = Pig(name="molly", color="blue", weight="3000 gr")


print(sharik.cat_biography())


