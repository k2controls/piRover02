''' Dog class to demonstrate Python classes'''

class Dog:
    name = None
    age = None
    breed = None


    def bark():
        print("Woof!")

    def set_age(self, people_years):
        self.age = 7 * people_years


my_dog = Dog()
your_dog = Dog()
my_dog.name = "Spot"
my_dog.set_age(2)
print(f"my dog's age is {my_dog.age}")
