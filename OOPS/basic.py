class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor method (initializes instance attributes)
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.age} says woof!"

# Create two objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5

# # Call methods
print(dog1.bark())  # Output: Buddy says woof!
print(dog2.bark())  # Output: Max says woof!
