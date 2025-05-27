
zahlen = []


while True:
    eingabe = input("Gib eine ganze Zahl ein (oder 'stop' zum Beenden): ")
    if eingabe.lower() == "stop":
        break
    try:
        zahl = int(eingabe)
        zahlen.append(zahl)
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl oder 'stop' ein.")

if zahlen:
    
    minimum = zahlen[0]
    maximum = zahlen[0]
    summe = 0

    for zahl in zahlen:
        if zahl < minimum:
            minimum = zahl
        if zahl > maximum:
            maximum = zahl
        summe += zahl

    durchschnitt = round(summe / len(zahlen), 2)
    zahlen.sort()

    print("Ergebnisse")
    print(f"Eingegebene Zahlen: {zahlen}")
    print(f"Kleinste Zahl: {minimum}")
    print(f"Größte Zahl: {maximum}")
    print(f"Durchschnitt: {durchschnitt}")
    print(f"Sortierte Liste (aufsteigend): {zahlen}")
else:
    print("Es wurden keine gültigen Zahlen eingegeben.")