import random   # Für zufällige Auswahl von Zeichen
import string   # liefert vorgefertigte Zeichenlisten (ascii_uppercase, digits, etc.)

def passwort_generator(laenge, grossbuchstaben=True, zahlen=True, sonderzeichen=True):
    zeichen = list(string.ascii_lowercase)

    if grossbuchstaben:
        zeichen += list(string.ascii_uppercase)
    if zahlen:
        zeichen += list(string.digits)
    if sonderzeichen:
        zeichen += list("!@#$%^&*()-_")

    if not zeichen:
        return "Fehler: Keine Zeichengruppe ausgewählt!"
    
    passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
    return passwort

# Interaktiv testen
try:
    laenge = int(input("Wie lang soll das Passswort sein? "))
    gross = input("Großbuchstaben? (ja/nein): ").lower() == "ja"
    zahlen = input("Zahlen? (ja/nein): ").lower() == "ja"
    sonder = input("Sonderzeichen? (ja/nein): ").lower() == "ja"
    #Ausgabe
    print("Dein Passwort:", passwort_generator(laenge, gross, zahlen, sonder))
except:
    print("⚠️ Ungültige Eingabe.")