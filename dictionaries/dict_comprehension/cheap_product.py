# Nur günstige Produkte übernehmen
produkte = {
    "T-Shirt": 19.99,
    "Sneaker": 89.95,
    "Hose": 45.00,
    "Mütze": 9.50
}
günstige_produkte = {produkt: preis for produkt, preis in produkte.items() if preis < 50.00}
print(f"Günstige Produkte: {günstige_produkte}")