eingabe = int(input("Bitte gib deine Schulnote ein: "))

note = int(eingabe)

if note == 1:
            ausgabe = "sehr gut"
elif note == 2:
            ausgabe = "gut"
elif note == 3:
            ausgabe = "befriedigend"
elif note == 4:
            ausgabe = "ausreichend"
elif note == 5:
            ausgabe = "mangelhaft"
elif note == 6:
            ausgabe = "ungenügend"
print(f"Die Note {note} entspricht: {ausgabe}")
