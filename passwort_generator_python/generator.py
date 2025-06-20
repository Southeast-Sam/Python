import random
import string

def passwort_generator(laenge, grossbuchstaben=True, zahlen=True, sonderzeichen=True):
    zeichen = list(string.ascii_uppercase)

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
    gross = input("Großbuchstaben? (j/n): ").lower() == "j"
    zahlen = input("Zahlen? (j/n): ").lower() == "j"
    sonder = input("Sonderzeichen? (j/n): ").lower() == "j"

    print("Dein Passwort:", passwort_generator(laenge, gross, zahlen, sonder))
except:
    print("⚠️ Ungültige Eingabe.")