# Kategorisiertes Layout
kategorien = {
    "obst": ["Apfel", "Banane", "Orange"],
    "gemüse": ["Karotte", "Gurke", "Tomate"]
}

# Zuweisung eine neue Kategorie hinzufügen
kategorien["getränke"] = ["Wasser", "Tee", "Saft"] # ["getränke"] -> [] ist ein Subscription-Operator

for kategorie, items in kategorien.items():
    print(f"{kategorie.capitalize()}:")
    for item in items:
        print(" -", item)
    print() # Leerzeile

# den Nutzer nach ein Item abfragen
auswahl = input("Welche Kategorie möchtest du anzeigen? ")
if auswahl in kategorien:
    for item in kategorien[auswahl]:
        print(item)
else:
    print("Kategorie nicht gefunden.")