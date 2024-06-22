class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def nama(self):
      print("Hello")

class Cat:
  def __init__(self, nama):
    self.nama2 = nama
    
  def sound2(self):
    print(f"The cat meows1 {self.nama2}")

# Example usage
dog = Dog("Fido")
cat = Cat("Whiskers")

dog.sound()  # Output: The dog barks.
cat.sound2()  # Output: The cat meows.
