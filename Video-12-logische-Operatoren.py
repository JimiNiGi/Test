
print("Willkommen in der Lotterie!")
number1 = int(input("Bitte wähle eine Zahl zwischen 1 und 49: "))
number2 = int(input("Bitte wähle eine Zahl zwischen 1 und 49: "))
number3 = int(input("Bitte wähle eine Zahl zwischen 1 und 49: "))

#Gewinnzahl 1: 3
#Gewinnzahl 2: 14
#Gewinnzahl 3: 22

if number1 == 3 and number2 == 14 and number3 == 22:
    print("Du hast gewonnen, Herzlichen Glückwunsch!")
else:
    print("Du hast leider verloren...")
    print("Versuche es nochmal")