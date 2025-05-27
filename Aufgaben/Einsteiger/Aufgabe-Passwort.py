benutzername = input("Bitte gib Benutzernamen ein: ")
passwort = input("Bitte gib dein Passwort ein: ")

if benutzername == "Benutzername" and passwort == "geheim":
    print("Login erfolgreich!")
else:
    print("Login fehlgeschlagen. Benutzername oder Passwort ist falsch.")