# Noten-Liste
noten = {
    "Ali": 2.0,
    "Lea": 1.7,
    "Amir": 3.3,
    "Sara": 1.3,
    "Jonas": 4.0
}
for name, note in noten.items():
    print(f"{name} hat die Note {note:.1f}")

# Nur die Schüler mit Note < 3.0 ausgeben
print("Die folgenden Schüler sind bestanden:")
for name, note in noten.items():
    if note < 3.0:
        print(f"{name}")

# Durchschnitt aller Noten berechnen
durchschnitt = sum(noten.values()) / len(noten)
print(f"Der Durchschnitt aller Noten ist: {durchschnitt:.2f}")