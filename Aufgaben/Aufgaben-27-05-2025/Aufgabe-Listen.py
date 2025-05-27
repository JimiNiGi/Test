
zahlen = [4, 7, 2, 9, 1, 5, 3]

laenge = len(zahlen)
groesste_zahl = max(zahlen)
kleinste_zahl = min(zahlen)

print("Aufgabe: Einfach")

print(f"Länge der Liste: {laenge}")
print(f"Größte Zahl: {groesste_zahl}")
print(f"Kleinste Zahl: {kleinste_zahl}")

durchschnitt = sum(zahlen) / laenge
umgekehrte_liste = zahlen[::-1]

print("Aufgabe: Mittel")

print(f"Durchschnitt der Zahlen: {durchschnitt}")
print(f"Liste in umgekehrter Reihenfolge: {umgekehrte_liste}")

gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]

print("Aufgabe: Experte")
print(f"Liste der geraden Zahlen: {gerade_zahlen}")