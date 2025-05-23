farbe = "blau"
groesse = "groß"
anzahl_tueren = 3
kraftstoffart = "Diesel"
fahrzeugtyp = "Lkw"
baujahr = 2022
kilometerstand = 55000
reifenhersteller = "Michelin"
modellbezeichnung = "Actros"
hubraum_liter = 12.8

print("Ursprüngliche Fahrzeugdetails:")
print(f"Farbe: {farbe}")
print(f"Größe: {groesse}")
print(f"Anzahl Türen: {anzahl_tueren}")
print(f"Kraftstoffart: {kraftstoffart}")
print(f"Fahrzeugtyp: {fahrzeugtyp}")
print(f"Baujahr: {baujahr}")
print(f"Kilometerstand: {kilometerstand}")
print(f"Reifenhersteller: {reifenhersteller}")
print(f"Modellbezeichnung: {modellbezeichnung}")
print(f"Hubraum (Liter): {hubraum_liter}")

print("\nVor dem Tausch:")
print(f"Farbe: {farbe}")
print(f"Fahrzeugtyp: {fahrzeugtyp}")

temp_farbe = farbe
farbe = fahrzeugtyp
fahrzeugtyp = temp_farbe

print("\nNach dem Tausch:")
print(f"Farbe: {farbe}")
print(f"Fahrzeugtyp: {fahrzeugtyp}")