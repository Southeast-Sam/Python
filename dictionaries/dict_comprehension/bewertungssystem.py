# Bewertungssystem mit Note & Prädikat
punkte = {
    "Ali": 92,
    "Bora": 77,
    "Cem": 58,
    "Dina": 46,
    "Elif": 33
}

# dict comprehension zur Umwandlung in Noten mit Prädikat
noten = {
    name: (
        "Note 1 - Sehr gut" if punktzahl >= 90 else
        "Note 2 - Gut" if punktzahl >= 75 else
        "Note 3 - Befriedigend" if punktzahl >=60 else
        "Note 4 - Ausreichend" if punktzahl >= 45 else
        "Note 5 - Mangelhaft"
    )
    for name, punktzahl in punkte.items()
}

# Ausgabe
print("Bewertungen:")
for name, bewertung in noten.items():
    print(f"{name}: {bewertung}")