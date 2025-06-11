# Produkte kategorisieren
produkte = {
    "T-Shirt": 19.99,
    "Sneaker": 89.95,
    "Hose": 45.00,
    "Mütze": 9.50
}
# Erstelle ein neues Dict produkt_kategorien, in dem jedem Produkt eine Kategorie zugewiesen wird: "günstig", "mittel", "teuer"
produkt_kategorien = {
    produkt: "günstig" if preis < 20 else "mittel" if preis < 50 else "teuer" for produkt, preis in produkte.items()
}
print(f"Produktkategorien: {produkt_kategorien}")