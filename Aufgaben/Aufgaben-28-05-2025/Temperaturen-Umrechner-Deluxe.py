import os

# ANSI-Escape-Codes für Farben und Formatierung
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def celsius_zu_fahrenheit(c):
    """Wandelt eine Temperatur von Celsius in Fahrenheit um."""
    try:
        c = float(c)
        f = c * 9/5 + 32
        return f"{f:.2f}"  # Formatierung auf 2 Dezimalstellen
    except ValueError:
        return f"{RED}Ungültige Eingabe. Bitte geben Sie eine Zahl ein.{RESET}"

def fahrenheit_zu_celsius(f):
    """Wandelt eine Temperatur von Fahrenheit in Celsius um."""
    try:
        f = float(f)
        c = (f - 32) * 5/9
        return f"{c:.2f}"  # Formatierung auf 2 Dezimalstellen
    except ValueError:
        return f"{RED}Ungültige Eingabe. Bitte geben Sie eine Zahl ein.{RESET}"

def temperatur_umrechner():
    """Hauptfunktion des Temperaturumrechners."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Bildschirm leeren
    print(f"\n{BOLD}{CYAN}🌡️ Willkommen zum ✨ Temperatur-Umrechner Deluxe ✨ 🌡️{RESET}\n")

    while True:
        print(f"{BOLD}Bitte wählen Sie eine Umrechnungsrichtung:{RESET}")
        print(f"  {GREEN}1{RESET} - Celsius nach Fahrenheit")
        print(f"  {YELLOW}2{RESET} - Fahrenheit nach Celsius")
        print(f"  {RED}3{RESET} - {BOLD}Beenden{RESET}")

        auswahl = input(f"{BOLD}Ihre Auswahl ({GREEN}1{RESET}, {YELLOW}2{RESET} oder {RED}3{RESET}): {RESET}")

        if auswahl == '1':
            celsius_eingabe = input("Geben Sie die Temperatur in Celsius ein: ")
            fahrenheit_ergebnis = celsius_zu_fahrenheit(celsius_eingabe)
            if isinstance(fahrenheit_ergebnis, str):
                print(f"  {fahrenheit_ergebnis}\n")
            else:
                print(f"  {celsius_eingabe}°C sind {BOLD}{GREEN}{fahrenheit_ergebnis}°F{RESET}\n")
        elif auswahl == '2':
            fahrenheit_eingabe = input("Geben Sie die Temperatur in Fahrenheit ein: ")
            celsius_ergebnis = fahrenheit_zu_celsius(fahrenheit_eingabe)
            if isinstance(celsius_ergebnis, str):
                print(f"  {celsius_ergebnis}\n")
            else:
                print(f"  {fahrenheit_eingabe}°F sind {BOLD}{YELLOW}{celsius_ergebnis}°C{RESET}\n")
        elif auswahl == '3':
            print(f"\n{BOLD}{CYAN}👋 Vielen Dank für die Nutzung des ✨ Temperatur-Umrechners Deluxe ✨! 👋{RESET}\n")
            break
        else:
            print(f"{RED}Ungültige Auswahl. Bitte wählen Sie {GREEN}1{RESET}, {YELLOW}2{RESET} oder {RED}3{RESET}.{RESET}\n")

if __name__ == "__main__":
    temperatur_umrechner()