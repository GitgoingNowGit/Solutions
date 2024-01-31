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
    def check(self):
        # if morris.sleepiness < 0:
        #     morris.sleepiness = 0
        # if morris.thirst < 0:
        #     morris.thirst = 0
        # if morris.hunger < 0:
        #     morris.hunger = 0
        # if morris.whisky < 0:
        #     morris.whisky = 0
        # if morris.gold < 0:
        #     morris.gold = 0
        if morris.sleepiness > 84:
            morris.sleep()
            morris.sleep()
        if morris.hunger > 95:
            morris.eat()
        if morris.thirst > 95 and morris.gold > 0:
            morris.buy_whisky()
            morris.drink()

    def sleep(self):
        morris.sleepiness -= 10
        morris.thirst += 1
        morris.hunger += 1

    def mine(self):
        morris.sleepiness += 5
        morris.thirst += 5
        morris.hunger += 5
        morris.gold += 5

    def drink(self):
        if morris.whisky > 0:
            morris.thirst -= 15
            morris.sleepiness += 5
            morris.hunger += 1
            morris.whisky -= 1

    def eat(self):
            morris.hunger -= 20
            morris.thirst += 5
            morris.gold -= 2
            morris.sleepiness += 5

    def buy_whisky(self):
        if morris.gold > 0:
            morris.sleepiness += 5
            morris.thirst += 1
            morris.hunger += 1
            morris.whisky += 1
            morris.gold -= 1


    def __init__(self, sleepiness=0, thirst=0, hunger=0, whisky=0, gold=0, turn=0):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold
        self.turn = turn
def dead():
    return morris.sleepiness > 99 or morris.thirst > 99 or morris.hunger > 99

morris = Miner() #morris is very stupid and won't accept that he is a giant retarded pile of dumpster code, so he mines, killing himself slowly (but now he is a little smarter)

while not dead() and morris.turn < 1000:
    morris.mine()
    morris.check()
    morris.turn += 1
    print("Morris sleepiness:", morris.sleepiness, "Morris thirst:", morris.thirst, "Morris hunger:", morris.hunger, "Morris whisky:", morris.whisky,"Morris gold:",morris.gold,"Morris turn:",morris.turn)
else:
    print("### Morris died or the turn limit of 1000 was met. ###")
