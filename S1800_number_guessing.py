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

black = 0
white = 0
def calculate_coins(guess, answer):
    global white
    global black
    for cifre in guess:
        if cifre in answer:
            white += 1
    for guess_cifre, answer_cifre in zip(guess, answer):
        if guess_cifre == answer_cifre:
            black += 1
    white -= black
    return white, black

print(f'This is a guessing game. Your task is to guess a four digit integer between {start} and {end}.\n\nIf you guess the correct number, you will recieve a black coin.\nAnd if you guess a correct number, but in the wrong order you will recieve a weiss coin.\nYour score will be displayed at the end.\n')
answer = str(random.randint(start,end))
answer = '1234'
attempts = 0
while black <= 4:
    guess = input(f'Enter your guess here: ')
    white, black = calculate_coins(guess, answer)
#if 4 black coins congratulate the player, end game
#if between 0 and 3 black coins, print out number of black and white coins, and prompt player to guess again
#do this until the player gets 4 black coins
    if guess == answer:
       print(f'You guessed the correct numbr! +1 schwarz coin ({black})')
    elif guess in answer:
     print(f'You guessed partially correct, right number but wrong order. +1 weiss coin ({white})')
     attempts += 1
    else:
        attempts += 1
print(f'\nCongratulations you fool.\nYou got a total of {black} black coins, and a total of {white} white coins.\nIt took you {attempts} attempts to guess the correct number.')
print('Now, please stop gambling your lifesavings, this isnt one of "those" casinos.')

# guess = input(f'\nEnter your guess for the second digit here: ')
# if int(str(guess)) == int(str(answer)[1:2]):
#     print("You guessed the correct number! +1 schwarz coin")
# else:
#     print(f'You guessed wrong, the correct number was {int(str(answer)[1:2])}')
