class Animal:
    def __init__(self, name):
        self.is_alive = True
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


class Eagle(Animal):
    def fly(self):
        print(f"{self.name} is flying.")


class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming.")


dog = Dog("jack")
fish = Fish("nemo")
eagle = Eagle("garuda")

print(dog.is_alive)
fish.swim()
eagle.fly()
