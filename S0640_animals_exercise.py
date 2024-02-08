"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.


Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en klassemetode ved navn wag_tail for Dog.
    Denne metode udskriver i konsollen noget i stil med
    "Hunden Snoopy vifter med sin 32 cm lange hale"
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google det først.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random

class Animal():
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female
    def makenoise(self):
        print(f"You hear an unspecified animal noise")

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep


    def __repr__(self):
             return f"The dog goes {self.sound}. It is {self.height}cm tall. It weighs {self.weight}kg, and it has {self.legs} legs."

    def makenoise(self):
        print(f"You hear a dog")

    def wag_tail(self):
        return f"the dog {self.name} wags their {self.tail_length}cm long tail"

    # def hunts_sheep(self):
    #         if Dog("ziggy", "wof", 4, 50,4, False):
    #             return True
    #         else:
    #             return False
class Cat(Animal):

    def makenoise(self):
        print("You hear a cat")

dacat = Cat("Cat", "miaw", 3, 35, 4, True)
ziggy = Dog("ziggy","wof",4,50,4,False, 9000, True) #https://hq.ax/c6R
dadog = Dog("cheeseburger","wof",4,40,4,True, 6, False)

rand_bool = random.choice([True,False])
def mate(mother, father):
    if mother.female and not father.female:
        return f"puppyoso", "Moo",random.random(),random.randint(4,9),random.randint(2,4),rand_bool,random.randrange(3,8),rand_bool

animallist = [ziggy, dadog,dacat]
for animal in animallist:
    animal.makenoise()
print(ziggy.wag_tail())
mate(dadog, ziggy)