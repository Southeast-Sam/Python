"""
# 1. Liste mit mehreren Nutzern (Wiederholung + append())
alle_nutzer = []
for i in range(3): # läuft 3 mal: i = 0, 1, 2
    name = input("Wie heißt du?")
    alter = int(input("Wie alt bist du?"))
    nutzer = [name, alter]
    alle_nutzer.append(nutzer)
    print("Alle Nutzer:", alle_nutzer)
"""

"""
# 2. Zahlenausgabe mit Schleife
n = int(input("Bis wohin soll gezählt werden? "))

for i in range(1, n + 1):
    print(i)
"""

"""
# 3. Gerade zahlen zählen
for i in range(2, 20, 2):
    print(i)
"""

"""
# 4. Zahlen rückwärts zählen
for i in range(10, 0, -1):
    print(i)
"""

"""
# 5. Wörter einzeln ausgeben
obst = ["Apfel", "Banane", "Kirsche"]

for i in range(len(obst)):
    print(obst[i])
"""

"""
# 6. Nur kurze Wörter

tiere = ["Hund", "Elefant", "Katze", "Ameise", "Frosch"]

for tier in tiere:
    if len(tier) <= 5:
        print(tier)
"""

# 7. Nur ungerade Zahlen
for i in range(1, 20):
    if i % 2 == 1:
        print(i)