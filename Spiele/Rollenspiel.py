import random
import time

# --- Globale Variablen und Konstanten ---
HEILTRANK_WIRKUNG = 20
MANATRANK_WIRKUNG = 30
VERGIFTUNGS_SCHADEN = 4
VERGIFTUNGS_DAUER = 6
KRITISCHER_SCHLAG_CHANCE = 0.25
KRITISCHER_SCHLAG_FAKTOR = 3
AUSWEICH_CHANCE = 0.2
BESONDERE_AKTIONEN_CHANCE = 0.25  # Erhöhte Chance für spezielle Gegneraktionen
MAGIE_CHANCE = 0.15  # Chance für magische Effekte im Kampf
MANA_KOSTEN_ZAUBER = 20

# --- Hilfsfunktionen (unverändert) ---
def eingabe_aufforderung(prompt, optionen):
    while True:
        print(prompt)
        for i, option in enumerate(optionen):
            print(f"{i+1}. {option}")
        wahl = input("Deine Wahl: ")
        if wahl.isdigit() and 1 <= int(wahl) <= len(optionen):
            return int(wahl) - 1
        else:
            print("Ungültige Eingabe.")

def nachricht_anzeigen(nachricht, verzoegerung=0.2):
    print(nachricht)
    time.sleep(verzoegerung)

def inventar_anzeigen(spieler):
    nachricht_anzeigen("\n--- Dein Inventar ---")
    if not spieler["inventar"]:
        nachricht_anzeigen("Dein Inventar ist leer.")
    else:
        for gegenstand, anzahl in spieler["inventar"].items():
            nachricht_anzeigen(f"- {gegenstand}: {anzahl}")
    nachricht_anzeigen(f"Gold: {spieler['gold']}")
    if spieler["klasse"] == "Magier":
        nachricht_anzeigen(f"Mana: {spieler['mana']}/{spieler['max_mana']}")

def status_anzeigen(spieler):
    nachricht_anzeigen("\n--- Dein Status ---")
    nachricht_anzeigen(f"Name: {spieler['name']}")
    nachricht_anzeigen(f"Klasse: {spieler['klasse']}")
    nachricht_anzeigen(f"Level: {spieler['level']}")
    nachricht_anzeigen(f"Erfahrung: {spieler['erfahrung']}/{spieler['erfahrung_benoetigt']}")
    nachricht_anzeigen(f"HP: {spieler['hp']}/{spieler['max_hp']}")
    nachricht_anzeigen(f"Angriff: {spieler['angriff']}")
    nachricht_anzeigen(f"Verteidigung: {spieler['verteidigung']}")
    if spieler["klasse"] == "Magier":
        nachricht_anzeigen(f"Mana: {spieler['mana']}/{spieler['max_mana']}")
    if spieler.get("vergiftet", 0) > 0:
        nachricht_anzeigen(f"Vergiftet für {spieler['vergiftet']} Runden.")

def level_up(spieler):
    spieler["level"] += 1
    hp_steigerung = random.randint(8, 12)
    angriff_steigerung = random.randint(2, 4)
    verteidigung_steigerung = 1 if random.random() < 0.7 else 2
    spieler["max_hp"] += hp_steigerung
    spieler["hp"] = spieler["max_hp"]
    spieler["angriff"] += angriff_steigerung
    spieler["verteidigung"] += verteidigung_steigerung
    spieler["erfahrung"] = 0
    spieler["erfahrung_benoetigt"] = spieler["level"] * 250
    nachricht_anzeigen(f"\nDu bist Level {spieler['level']} geworden!")
    nachricht_anzeigen(f"Deine maximalen HP haben sich um {hp_steigerung} erhöht.")
    nachricht_anzeigen(f"Dein Angriff hat sich um {angriff_steigerung} erhöht.")
    nachricht_anzeigen(f"Deine Verteidigung hat sich um {verteidigung_steigerung} erhöht.")
    if spieler["klasse"] == "Magier":
        mana_steigerung = random.randint(10, 15)
        spieler["max_mana"] += mana_steigerung
        spieler["mana"] += mana_steigerung
        nachricht_anzeigen(f"Dein maximales Mana hat sich um {mana_steigerung} erhöht.")

def erhalte_erfahrung(spieler, menge):
    spieler["erfahrung"] += menge
    nachricht_anzeigen(f"Du hast {menge} Erfahrungspunkte erhalten.")
    while spieler["erfahrung"] >= spieler["erfahrung_benoetigt"]:
        level_up(spieler)

# --- Charaktererstellung (erweitert) ---
def charakter_erstellung():
    name = input("Wie lautet dein Name, glorreicher Held? ")
    klassen = {"Krieger": {"hp": 35, "angriff": 8, "verteidigung": 6, "mana": 0, "start_ausruestung": ["Breitschwert", "Eisenrüstung"]},
               "Magier": {"hp": 25, "angriff": 10, "verteidigung": 4, "mana": 50, "start_ausruestung": ["Arkaner Stab", "Roben des Gelehrten", "Manatrank"]},
               "Schurke": {"hp": 30, "angriff": 9, "verteidigung": 5, "mana": 20, "start_ausruestung": ["Doppelklingen", "Schattenlederrüstung", "Heiltrank"]}}
    wahl = eingabe_aufforderung("Wähle deine Klasse:", list(klassen.keys()))
    gewaehlte_klasse = list(klassen.keys())[wahl]
    werte = klassen[gewaehlte_klasse]
    nachricht_anzeigen(f"\nSeid gegrüßt, {name}, der/die meisterhafte {gewaehlte_klasse}!")
    spieler = {
        "name": name,
        "klasse": gewaehlte_klasse,
        "level": 1,
        "erfahrung": 0,
        "erfahrung_benoetigt": 250,
        "max_hp": werte["hp"],
        "hp": werte["hp"],
        "angriff": werte["angriff"],
        "verteidigung": werte["verteidigung"],
        "gold": 75,
        "mana": werte["mana"],
        "max_mana": werte["mana"],
        "inventar": {"Heiltrank": 2, "Manatrank": 1 if gewaehlte_klasse == "Magier" else 0},
        "aktueller_ort": "Sonnenfels",
        "quests": {} # Speichert aktive Quests
    }
    for ausruestung in werte["start_ausruestung"]:
        spieler["inventar"][ausruestung] = spieler["inventar"].get(ausruestung, 0) + 1
        if "Schwert" in ausruestung: spieler["angriff"] += 3
        if "Klinge" in ausruestung: spieler["angriff"] += 2
        if "Stab" in ausruestung: spieler["angriff"] += 4
        if "Rüstung" in ausruestung and "Leder" in ausruestung: spieler["verteidigung"] += 2
        if "Rüstung" in ausruestung and "Eisen" in ausruestung: spieler["verteidigung"] += 3
        if "Robe" in ausruestung: spieler["verteidigung"] += 1
    return spieler

# --- Quests (erweitert) ---
quests = {
    "Goblininvasion": {
        "beschreibung": "Der Bürgermeister von Sonnenfels bittet dich, 10 aggressive Goblin-Krieger in den Smaragdgrünen Hügeln zu vertreiben.",
        "ziel": {"typ": "gegner", "name": "Goblin-Krieger", "anzahl": 10},
        "belohnung": {"erfahrung": 600, "gold": 175, "gegenstand": "Axt des Waldläufers"}
    },
    "Diebstahl der Artefakte": {
        "beschreibung": "Die Priesterin des Mondtempels beklagt den Verlust heiliger Artefakte, gestohlen von Kobold-Minenarbeitern aus den Minen von Azurit.",
        "ziel": {"typ": "ort", "name": "Minen von Azurit", "aktion": "finde_artefakte"},
        "belohnung": {"erfahrung": 850, "gold": 225, "gegenstand": "Amulett der Weisheit"}
    },
    "Rettet die Kräuterkundige": {
        "beschreibung": "Eine mächtige Oger-Häuptlingin hat die Kräuterkundige des Dorfes in den Sümpfen der Verzweiflung gefangen genommen.",
        "ziel": {"typ": "gegner", "name": "Oger-Häuptlingin", "anzahl": 1, "ort": "Sümpfe der Verzweiflung", "ort_spezifisch": True},
        "belohnung": {"erfahrung": 1100, "gold": 275, "gegenstand": "Ring der Regeneration"}
    },
    "Das Verfluchte Medaillon": {
        "beschreibung": "Ein Händler in Sonnenfels bittet dich, ein verfluchtes Medaillon aus den Ruinen von Eldoria zu bergen.",
        "ziel": {"typ": "ort", "name": "Ruinen von Eldoria", "aktion": "finde_medaillon"},
        "belohnung": {"erfahrung": 900, "gold": 250, "gegenstand": "Talisman des Schutzes"}
    }
}

def zeige_quests(spieler):
    nachricht_anzeigen("\n--- Deine aktuellen Aufgaben ---")
    if not spieler["quests"]:
        nachricht_anzeigen("Du hast keine aktiven Aufgaben.")
    else:
        for name, quest_status in spieler["quests"].items():
            quest = quests[name]
            fortschritt = ""
            if quest_status.get("fortschritt"):
                if quest["ziel"]["typ"] == "gegner":
                    fortschritt = f"({quest_status['fortschritt']}/{quest['ziel']['anzahl']})"
                elif quest["ziel"]["typ"] == "ort" and quest_status.get("erfuellt"):
                    fortschritt = "(Erfüllt)"
            ort_hinweis = f" (im/in den {quest['ziel'].get('ort', '')})" if quest["ziel"].get("ort_spezifisch") or quest["ziel"].get("ort") else ""
            nachricht_anzeigen(f"- {name}: {quest['beschreibung']} {fortschritt}{ort_hinweis}")

def quest_annehmen(spieler, quest_name):
    if quest_name in quests and quest_name not in spieler["quests"]:
        spieler["quests"][quest_name] = {"aktiv": True, "fortschritt": 0}
        nachricht_anzeigen(f"Du hast die Aufgabe '{quest_name}' angenommen.")
    else:
        nachricht_anzeigen("Diese Aufgabe ist nicht verfügbar oder du hast sie bereits angenommen.")

def quest_fortschritt(spieler, ziel_typ, ziel_name):
    for name, status in spieler["quests"].items():
        quest = quests[name]
        if quest["ziel"]["typ"] == ziel_typ and quest["ziel"]["name"] == ziel_name:
            if ziel_typ == "gegner" and (not quest["ziel"].get("ort_spezifisch") or spieler["aktueller_ort"] == quest["ziel"].get("ort")):
                spieler["quests"][name]["fortschritt"] += 1
                nachricht_anzeigen(f"Fortschritt bei Aufgabe '{name}': {spieler['quests'][name]['fortschritt']}/{quest['ziel']['anzahl']}")
                if spieler["quests"][name]["fortschritt"] >= quest["ziel"]["anzahl"]:
                    quest_abschliessen(spieler, name)
            elif ziel_typ == "ort" and quest["ziel"].get("aktion") == ziel_name.lower().replace(" ", "_") and spieler["aktueller_ort"] == quest["ziel"]["name"]:
                spieler["quests"][name]["erfuellt"] = True
                nachricht_anzeigen(f"Du hast das Ziel der Aufgabe '{name}' erreicht.")

def quest_abschliessen(spieler, quest_name):
    if quest_name in spieler["quests"] and (spieler["quests"][quest_name].get("fortschritt", 0) >= quests[quest_name]["ziel"]["anzahl"] or spieler["quests"][quest_name].get("erfuellt")):
        belohnung = quests[quest_name]["belohnung"]
        nachricht_anzeigen(f"\n--- Aufgabe '{quest_name}' abgeschlossen! ---")
        erhalte_erfahrung(spieler, belohnung["erfahrung"])
        spieler["gold"] += belohnung["gold"]
        nachricht_anzeigen(f"Du hast {belohnung['gold']} Gold erhalten.")
        if "gegenstand" in belohnung:
            spieler["inventar"][belohnung["gegenstand"]] = spieler["inventar"].get(belohnung["gegenstand"], 0) + 1
            nachricht_anzeigen(f"Du hast '{belohnung['gegenstand']}' erhalten.")
        del spieler["quests"][quest_name]
    else:
        nachricht_anzeigen(f"Du hast die Aufgabe '{quest_name}' noch nicht abgeschlossen.")

# --- Orte und Interaktionen (noch weiter erweitert) ---
orte = {
    "Sonnenfels": {
        "beschreibung": "Eine lebendige Stadt am Fuße des majestätischen Sonnenberges.",
        "optionen": [
            {"text": "Den Marktplatz besuchen", "ziel": "Marktplatz"},
            {"text": "Die Heilige Halle aufsuchen", "aktion": "sprich_priesterin"},
            {"text": "In die Smaragdgrünen Hügel aufbrechen", "ziel": "Smaragdgruene_Huegel"},
            {"text": "Die Taverne 'Zum Goldenen Krug' besuchen", "aktion": "besuche_taverne"},
            {"text": "Aktive Aufgaben ansehen", "aktion": "zeige_quests"}
        ]
    },
    "Marktplatz": {
        "beschreibung": "Ein quirliger Ort des Handels. Hier findest du alles von Waffen bis zu Tränken.",
        "optionen": [
            {"text": "Mit dem Schmied handeln", "aktion": "handle_schmied"},
            {"text": "Beim Alchemisten einkaufen", "aktion": "kaufe_traenke"},
            {"text": "Zurück nach Sonnenfels", "ziel": "Sonnenfels"}
        ]
    },
    "Smaragdgruene_Huegel": {
        "beschreibung": "Sanfte, grüne Hügel, durchzogen von kleinen Bächen. Hier treiben sich oft Goblins herum.",
        "optionen": [
            {"text": "Die Hügel weiter erkunden", "ziel": "Smaragdgruene_Huegel"},
            {"text": "Einen alten Steinkreis untersuchen", "aktion": "untersuche_steinkreis", "chance": 0.4},
            {"text": "Zurück nach Sonnenfels", "ziel": "Sonnenfels"}
        ],
        "zufallsbegegnung_chance": 0.7,
        "monster": [{"name": "Goblin-Krieger", "hp": 40, "angriff": 7, "verteidigung": 3, "erfahrung": 90, "beute": ["Goblin-Ohr"], "beute_chance": 0.6}]
    },
    "Alter Steinkreis": {
        "beschreibung": "Ein mystischer Ort mit uralten Steinen, die in einem Kreis angeordnet sind. Magische Energie liegt in der Luft.",
        "optionen": [
            {"text": "Die Steine berühren", "aktion": "beruehre_steine"},
            {"text": "Zurück zu den Smaragdgrünen Hügeln", "ziel": "Smaragdgruene_Huegel"}
        ],
        "ereignisse": ["Du spürst einen kurzen Energieschub. (+5 Mana)", "Die Luft knistert magisch.", "Nichts Besonderes passiert."]
    },
    "Die Taverne 'Zum Goldenen Krug'": {
        "beschreibung": "Ein gemütlicher Treffpunkt für Abenteurer und Einheimische. Der Duft von gebratenem Fleisch liegt in der Luft" }
}