summe_gerade = 0

for zahl in range(2, 101, 2):
    summe_gerade += zahl

print(f"Die Summe der geraden Zahlen von 1 bis 100 beträgt: {summe_gerade}")

while True:
    try:
        obergrenze = int(input("Bis zu welcher Zahl sollen die geraden Zahlen summiert werden? "))
        if obergrenze >= 2:
            break
        else:
            print("Bitte gib eine Zahl größer oder gleich 2 ein.")
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

summe_gerade_benutzer = 0

for zahl in range(2, obergrenze + 1, 2):
    summe_gerade_benutzer += zahl

print(f"Die Summe der geraden Zahlen bis {obergrenze} beträgt: {summe_gerade_benutzer}")