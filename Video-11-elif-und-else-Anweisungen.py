
age = int(input("Bitte gebe dein Alter ein: "))

if age < 18:
    print("Achtung, der Nutzer ist jünger als 18")
    print("Das Programm zerstört sich in 3 Sekunden")
    print("3")
    print("2")
    print("1")
    print("Boom")
elif age == 18:
    print("Der Nutzer ist exakt 18")
    print("Sie sind zwar noch sehr jung aber Sie dürfen passieren")
    print("Willkommen")
    print("Wie kann ich Ihnen helfen?")

else:
    print("Der Nutzer ist volljährig")
    print("Willkommen")
    print("Wie kann ich Ihnen helfen?")
