# Wörter zählen
woerter = ["Apfel", "Banane", "Apfel", "Orange", "Banane", "Banane"]
woerter_zaehlen = {wort: woerter.count(wort) for wort in set(woerter)}  # set() entfernt Duplikate
print(f"Wörter zählen: {woerter_zaehlen}")