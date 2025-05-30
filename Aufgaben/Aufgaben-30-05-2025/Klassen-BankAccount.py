class BankAccount:
    def __init__(self, kontoinhaber, ueberziehungsrahmen=-100.0):
        """
        Initialisiert ein neues BankAccount-Objekt.

        Args:
            kontoinhaber (str): Der Name des Kontoinhabers.
            ueberziehungsrahmen (float, optional): Das Überziehungslimit des Kontos.
                                                   Standardmäßig -100.0 €.
        """
        self.kontoinhaber = kontoinhaber
        self.kontostand = 0.0
        self.ueberziehungsrahmen = ueberziehungsrahmen

    def einzahlen(self, betrag):
        """
        Erhöht den Kontostand um den übergebenen Betrag.

        Args:
            betrag (float): Der Betrag, der eingezahlt werden soll.
        """
        if betrag > 0:
            self.kontostand += betrag
            print(f"Einzahlung von {betrag:.2f} € erfolgreich.")
        else:
            print("Ungültiger Betrag. Bitte geben Sie einen positiven Betrag ein.")

    def abheben(self, betrag):
        """
        Verringert den Kontostand um den übergebenen Betrag, wenn genügend Geld vorhanden ist
        (unter Berücksichtigung des Überziehungslimits).

        Args:
            betrag (float): Der Betrag, der abgehoben werden soll.
        """
        if betrag > 0:
            if self.kontostand - betrag >= self.ueberziehungsrahmen:
                self.kontostand -= betrag
                print(f"Abhebung von {betrag:.2f} € erfolgreich.")
            else:
                print("Abhebung nicht möglich. Verfügbares Guthaben überschritten (inkl. Überziehungslimit).")
        else:
            print("Ungültiger Betrag. Bitte geben Sie einen positiven Betrag ein.")

    def zeige_kontostand(self):
        """
        Gibt den aktuellen Kontostand aus.
        """
        print(f"Aktueller Kontostand: {self.kontostand:.2f} €")

    def zinsen_berechnen(self, zinssatz):
        """
        Berechnet und fügt Zinsen zum Kontostand hinzu, wenn der Kontostand positiv ist.

        Args:
            zinssatz (float): Der jährliche Zinssatz in Prozent (z.B. 1.5 für 1.5%).
        """
        if self.kontostand > 0:
            zinsen = self.kontostand * (zinssatz / 100)
            self.kontostand += zinsen
            print(f"Zinsen in Höhe von {zinsen:.2f} € wurden gutgeschrieben.")
        else:
            print("Keine Zinsgutschrift möglich, da der Kontostand nicht positiv ist.")

    def __str__(self):
        """
        Gibt eine lesbare String-Repräsentation des Bankkontos zurück.
        """
        return f"Konto von {self.kontoinhaber} – Kontostand: {self.kontostand:.2f} € – Überziehungslimit: {self.ueberziehungsrahmen:.2f} €"

# Beispielhafte Nutzung der Klasse
if __name__ == "__main__":
    mein_konto = BankAccount("Max Mustermann")
    print(mein_konto)  # Gibt die __str__ Repräsentation aus

    mein_konto.einzahlen(100.0)
    mein_konto.zeige_kontostand()

    mein_konto.abheben(50.0)
    mein_konto.zeige_kontostand()

    mein_konto.abheben(200.0) # Nun sollte eine Warnung kommen da man ins Minus geht 

    mein_konto_mit_limit = BankAccount("Erika Beispiel", -200.0)
    mein_konto_mit_limit.einzahlen(50.0)
    mein_konto_mit_limit.abheben(230.0) # Sollte funktionieren, da das Limit berücksichtigt wird
    mein_konto_mit_limit.zeige_kontostand()

    mein_konto.zinsen_berechnen(2.0)
    mein_konto.zeige_kontostand()