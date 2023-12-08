"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum ofile_w_names.txtg et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.

plagarisme? 🤷‍♂️
"""

maybemyfile = "file_w_namesX.txt"
line_numberbruh = 0

with open(maybemyfile) as file:
    for line in file:
         line_numberbruh += 1
         line2 = line.split(",", 1)
         print(f" Target 2: {line_numberbruh}: {line2}")
         line3 = []
         for x in line2:
            line3.append(x.strip())
            print(f" Target 3: {line_numberbruh}: {line3}")

