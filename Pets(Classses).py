class Pet:
  def __init__(self, pet_type, name, sound):
    self.pet_type = pet_type
    self.name = name
    self.sound = sound

  def speak(self):
    print(f"{self.name} goes {self.sound}!")

  def play(self):
    print(f"{self.name} is playing!")



my_pet = Pet("gecko", "Sammy", "gek")
my_pet.speak()


class Cat(Pet):
  def __init__(self, name, sound, coat_length):
    super().__init__("cat", name, sound)
    self.coat_length = coat_length
  
  def purr(self):
    print(f"{self.name} if purring.")

cat = Cat("Mittens", "Meow", "long")
cat.purr()

class Dog(Pet):
  def __init__(self, name, sound, size):
    super().__init__("dog", name, sound)
    self.size = size
  
  def speak(self):
    print(f"{self.name} the {self.size} dog goes {self.sound}!")

  def wag_tail(self):
    print(f"{self.name} is wagging its tail.")

dog = Dog("Cruiser", "Woof", "small")
dog.speak()
dog.wag_tail()
cat.speak()
cat.play()
