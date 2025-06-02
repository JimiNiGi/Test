# Importiere die BankAccount-Klasse aus der Datei bank_account.py
from bank_account import BankAccount

if __name__ == "__main__":
    mein_konto = BankAccount("Max Mustermann")
    print(mein_konto)

    mein_konto.einzahlen(100.0)
    mein_konto.zeige_kontostand()

    mein_konto.abheben(50.0)
    mein_konto.zeige_kontostand()

    mein_konto.abheben(200.0)

    mein_konto_mit_limit = BankAccount("Erika Beispiel", -200.0)
    mein_konto_mit_limit.einzahlen(50.0)
    mein_konto_mit_limit.abheben(230.0)
    mein_konto_mit_limit.zeige_kontostand()

    mein_konto.zinsen_berechnen(2.0)
    mein_konto.zeige_kontostand()