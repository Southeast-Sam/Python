"""
buchstaben = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# List comprehension zur Filterung von Vokalen
vokale = [buchstabe for buchstabe in buchstaben if buchstabe in 'aeiou']
print(vokale)"""

# Wörter mit gerader Buchstabenzahl
woerter = ["Hund", "Katze", "Elefant", "Tiger", "Löwe", "Esel", "Maus", "Kuh", "Nilpferd", "Affe"]
gerade_woerter = [wort for wort in woerter if len(wort) % 2 == 0]
print("Wörter mit gerader Buchstabenzahl:", gerade_woerter)