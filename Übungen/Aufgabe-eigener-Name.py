daten = {
    "Name": "Nico Gärtner",
    "Alter": 33,
    "Geschlecht": "männlich",
    "Größe": "1,83m",
    "Gewicht": "72",
    "Augenfarbe": "blau",
    "Haarfarbe": "blond",
    "Beruf": "System Administrator",
    "Hobby": "zocken",
    "Charaktereigenschaften": "humorvoll"
}

satz = f"{daten['Name']} ist {daten['Alter']} Jahre alt, {daten['Geschlecht']} und {daten['Größe']} groß. Er wiegt {daten['Gewicht']}kg, hat {daten['Augenfarbe']}e Augen und {daten['Haarfarbe']}e Haare. Von Beruf ist er {daten['Beruf']}, sein Hobby ist {daten['Hobby']} und er wird als {daten['Charaktereigenschaften']} beschrieben."

print(satz)