"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen drive_car()

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne S0420_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du stadig er gået i stå, skal du åbne S0430_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Team-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

def drive_car(car):
    if drive_car(bluecar):
        print(f"the blue car has", bluecar_wheels, "wheels. And max speed is", bluecar_maxspeed)
    elif drive_car(redcar):
        print(f"the red car has", redcar_wheels, "wheels. And max speed is", redcar_maxspeed)
    print("vroooom")

bluecar_wheels = 4
bluecar_maxspeed = 80
bluecar = bluecar_maxspeed + bluecar_wheels

redcar_wheels = 6
redcar_maxspeed = 90
redcar = redcar_maxspeed + redcar_wheels
car = bluecar or redcar


drive_car(car)
