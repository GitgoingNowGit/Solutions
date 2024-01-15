class Animal:
    def inspect(self):
        print("Thats an animal :)")
class Dog(Animal):
    def dance(self):
        print("That crazy dog is dancing")
    def inspect_closely(self):
        print("Thats a skinwalker (:")
McDog = Dog()

McDog.inspect()
McDog.dance()
McDog.inspect_closely()
