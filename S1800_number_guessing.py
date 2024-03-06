""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random

start = 1000
end = 9999
global schwarz_coin
global Weiss_coin

print(f'This is a guessing game. Your task is to guess a four digit integer between {start} and {end}. \nYou will guess the integers individually till you have all four digits.')
answer = random.randint(start,end)
guess = input('\nEnter your guess for the first number here: ')
if int(str(guess)) == int(str(answer)[:1]):
    print("You guessed the correct number! +1 schwarz coin")
else:
    print(f'You guessed wrong, the correct number was {int(str(answer)[0:1])}')

guess = input(f'\nEnter your guess for the second number here: ')
if int(str(guess)) == int(str(answer)[1:2]):
    print("You guessed the correct number! +1 schwarz coin")
else:
    print(f'You guessed wrong, the correct number was {int(str(answer)[1:2])}')
