def celsius_zu_fahrenheit(c):
    """Wandelt eine Temperatur von Celsius in Fahrenheit um."""
    try:
        c = float(c)
        f = c * 9/5 + 32
        return f
    except ValueError:
        return "Ungültige Eingabe. Bitte geben Sie eine Zahl ein."

def fahrenheit_zu_celsius(f):
    """Wandelt eine Temperatur von Fahrenheit in Celsius um."""
    try:
        f = float(f)
        c = (f - 32) * 5/9
        return c
    except ValueError:
        return "Ungültige Eingabe. Bitte geben Sie eine Zahl ein."

def temperatur_umrechner():
    """Hauptfunktion des Temperaturumrechners."""
    print("\n🌡️ Willkommen zum Temperaturumrechner! 🌡️\n")

    while True:
        print("Bitte wählen Sie eine Umrechnungsrichtung:")
        print("1. Celsius nach Fahrenheit")
        print("2. Fahrenheit nach Celsius")
        print("3. Beenden")

        auswahl = input("Ihre Auswahl (1, 2 oder 3): ")

        if auswahl == '1':
            celsius_eingabe = input("Geben Sie die Temperatur in Celsius ein: ")
            fahrenheit_ergebnis = celsius_zu_fahrenheit(celsius_eingabe)
            print(f"{celsius_eingabe}°C sind {fahrenheit_ergebnis}°F\n")
        elif auswahl == '2':
            fahrenheit_eingabe = input("Geben Sie die Temperatur in Fahrenheit ein: ")
            celsius_ergebnis = fahrenheit_zu_celsius(fahrenheit_eingabe)
            print(f"{fahrenheit_eingabe}°F sind {celsius_ergebnis}°C\n")
        elif auswahl == '3':
            print("👋 Vielen Dank für die Nutzung des Umrechners! 👋")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie 1, 2 oder 3.\n")

if __name__ == "__main__":
    temperatur_umrechner()