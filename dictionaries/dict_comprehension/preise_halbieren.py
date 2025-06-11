# Preise halbieren
preise = {
    "Apfel": 1.20,
    "Banane": 0.80,
    "Kirsche": 2.50
}
preise_halbiert = {obst: preis / 2 for obst, preis in preise.items()}
print(f"Halbierte Preise: {preise_halbiert}")