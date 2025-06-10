# Warenkorb & Rabatt anwenden
warenkorb = {
    "T-Shirt": 19.99,
    "Jeans": 49.90,
    "Sneaker": 89.95,
    "Mütze": 9.50
}

# Nutzer nach Rabatt fragen
rabatt = float(input("Rabatt in %: "))
if not (0 <= rabatt <= 100):  # Überprüfen, ob der Rabattwert gültig ist
    print("Ungültiger Rabattwert. Bitte einen Wert zwischen 0 und 100 eingeben.")
    exit()
# Rabtt in Dezimalfaktor umwandeln
faktor = 1 - rabatt / 100
# Alle Preise im Dictionary aktualisieren
for produkt in warenkorb:
    warenkorb[produkt] *= faktor
    # Ausgabe der aktualisierten Preise
for produkt, preis in warenkorb.items():
    print(f"{produkt}: {preis:.2f}€")
