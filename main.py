
class Animal:
    def inspect(self):
        print("Thats an animal :)")

class Dog(Animal):
    def dance(self):
        print("That crazy dog is dancing")

    def inspect_closely(self):
        print("Thats a skinwalker :,)")
        global owner_sanity
        owner_sanity += 51
        if owner_sanity > 100:
            print("You went insane, your sanity exceed 100. Your sanity:", owner_sanity)


McDog = Dog()
owner_sanity = 50


McDog.inspect()
McDog.dance()
McDog.inspect_closely()

