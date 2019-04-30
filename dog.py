class Dog:
    # Class attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

        # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

ballan = Dog("Ballan", 6)

print(ballan.description())
print(ballan.speak("boof"))