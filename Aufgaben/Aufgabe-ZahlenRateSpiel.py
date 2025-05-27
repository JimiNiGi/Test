import random

zufallszahl = random.randint(1, 100)
versuche = 0

print("Willkommen zum Zahlenratespiel!")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Rate mal!")

while True:
    try:
        benutzer_eingabe = int(input("Dein Tipp: "))
        versuche += 1

        if benutzer_eingabe < zufallszahl:
            print("Die Zahl ist größer.")
        elif benutzer_eingabe > zufallszahl:
            print("Die Zahl ist kleiner.")
        else:
            print(f"Super! Du hast die Zahl {zufallszahl} nach {versuche} Versuchen erraten!")
            break  # Beendet die Schleife, wenn die Zahl richtig geraten wurde

    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")