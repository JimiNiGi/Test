daten = {
    "Name": "Max Mustermann",
    "Alter": 30,
    "Geschlecht": "männlich",
    "Größe": "1,80m",
    "Gewicht": "75kg",
    "Augenfarbe": "braun",
    "Haarfarbe": "schwarz",
    "Beruf": "Softwareentwickler",
    "Hobby": "Lesen",
    "Charaktereigenschaften": "freundlich"
}

satz = f"{daten['Name']} ist {daten['Alter']} Jahre alt, {daten['Geschlecht']} und {daten['Größe']} groß. Er wiegt {daten['Gewicht']}kg, hat {daten['Augenfarbe']}e Augen und {daten['Haarfarbe']}e Haare. Von Beruf ist er {daten['Beruf']}, sein Hobby ist {daten['Hobby']} und er wird als {daten['Charaktereigenschaften']} beschrieben."

print(satz)