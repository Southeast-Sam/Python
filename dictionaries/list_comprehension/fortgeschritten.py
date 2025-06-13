# Flache Liste aus Matrix mit Bedingung
matrix = [
    [1, 4, 7],
    [9, 2, 11],
    [3, 5, 13]
]
matrix_flach = [zahl for zeile in matrix for zahl in zeile if (zahl > 5) % 2 == 1]
print("Flache Liste mit ungeraden Zahlen:", matrix_flach)


# Alle Kombinationen von zwei Listen als Tupel
farben = ["rot", "grün", "blau"]
formen = ["Kreis", "Quadrat"]
kombinationen = [(farbe, form) for farbe in farben for form in formen]
print("Alle Kombinationen von Farben und Formen:", kombinationen)


# Wörter umdrehen, die mit einem Vokal starten
woerter = ["Apfel", "Banane", "Orange","Uhr", "Erdbeere", "Kiwi"]
woerter_umgedreht = [wort[::-1] for wort in woerter if wort[0].lower() in "aeiou"]
print("Wörter umgedreht, die mit einem Vokal starten:", woerter_umgedreht)


# Primzahlen in Range mit List Comprehension, eine Liste mit allen Primzahlen zwischen 2 und 50
primzahlen = [
    zahl for zahl in range(2, 51)
    if all(zahl % i != 0 for i in range(2, int(zahl**0.5) + 1))
]
print("Primzahlen zwischen 2 und 50:", primzahlen)