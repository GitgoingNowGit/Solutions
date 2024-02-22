"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random

class Character:

    def __init__(self, profession, name, health, attackpower):
        self.profession = profession
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attackpower = attackpower

    def health_status(self):
        return f"{self.name} has {self._current_health} HP"

    def __repr__(self):
        return f"{self.profession} {self.name}: <max health = {self.max_health}>, <current health = {self._current_health}>, <attack power = {self.attackpower}>"

    def hit(self, other):
        print("\n", self.name, "hit", other.name+',', "inflicting damage of", self.attackpower, "HP on", other.name+".", "\n")
        other.get_hit(self.attackpower)
        # other._current_health -= self.attackpower

    def get_hit(self, attackpower):
        self._current_health -= attackpower

    # def heal(self,other):
    #     print("\n", self.name, "healed", other.name + ',', "mitigating damage of", self.attackpower, "HP on", other.name + ".", "\n")
    #     other.get_heal(self)
    # def get_heal(self, healpower):
    #     self._current_health += healpower

class Healer(Character):
    def __init__(self, profession, name, health, attackpower, healpower):
        super().__init__(profession, name, health, attackpower)
        self.healpower = healpower
        self._current_health = health

    def heal(self,other):
        print("\n", self.name, "healed", other.name + ',', "reversing damage of", self.attackpower, "HP on", other.name + ".", "\n")
        other.get_heal(self.healpower)

    def get_heal(self, healpower):
        self._current_health += healpower

# random.randint(10,14)
# def all_health():
#     characters = [arthur, marduk]
#     for character in characters:
#         print(character.health_status())

grisell = Character('Knight', 'Grissell',random.randint(95,145),14)
arthur = Character('Knight', 'Arthur', 120, random.randint(9, 11))
marduk = Character('Sorcerer', 'Marduk', 100, random.randint(10, 13))
althea = Healer('Healer', 'Althea', random.randint(68, 84), random.randint(11,15), 5)
rafael = Healer('Healer', 'Rafael', 92, 0, 4)
print(marduk)
arthur.hit(marduk)
print(rafael.health_status())
althea.heal(rafael)
print(rafael.health_status())
# all_health()