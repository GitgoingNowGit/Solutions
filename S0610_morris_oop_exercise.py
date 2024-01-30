"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner():


    def sleep(self):
        morris.sleepiness -= 10
        morris.thirst += 1
        if morris.sleepiness < 0:
            morris.sleepiness = 0
        print("M. slept")

    def mine(self):
        morris.sleepiness += 5
        morris.thirst += 5
        print("M. mined")

    def drink(self):
        if morris.whisky > 0 and morris.thirst > 0:
            morris.thirst -= 15
            morris.sleepiness += 5
        elif morris.thirst < 0:
            morris.thirst = 0
        print("M. drank")

    def eat(self):
        morris.hunger -= 20
        morris.thirst += 5


    def __init__(self, sleepiness=0, thirst=0, hunger=0, whisky=0, gold=0, turn=0):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold
        self.turn = turn


def dead():
    return morris.sleepiness > 100 or morris.thirst > 100 or morris.hunger > 100


morris = Miner()
#morris is very stupid and doesn't know he is a giant retarded pile of dumpster code, so he mines, killing himself slowly
while not dead() and morris.turn < 1000:
    morris.mine()
    morris.sleep()
    morris.drink()
    morris.turn += 1
    print("Morris sleepiness:", morris.sleepiness, "Morris thirst:", morris.thirst, "Morris hunger:", morris.hunger, "Turn:", morris.turn)
else:
    print("Morris died or the turn limit of 1000 was met.")
