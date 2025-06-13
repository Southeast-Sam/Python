# Rabattrechner
def rabattrechner(preis, rabatt_prozent):
    if preis < 0 or rabatt_prozent < 0:
        raise ValueError("Preis und Rabatt müssen positiv sein.")
    rabatt = preis * (rabatt_prozent / 100)
    endpreis = preis - rabatt
    return endpreis
# Beispielaufruf
if __name__ == "__main__":
    try:
        preis = float(input("Geben Sie den Preis ein: "))
        rabatt_prozent = float(input("Geben Sie den Rabatt in Prozent ein: "))
        endpreis = rabattrechner(preis, rabatt_prozent)
        print(f"Der Endpreis nach {rabatt_prozent}% Rabatt beträgt: {endpreis:.2f} Euro")
    except ValueError as e:
        print(f"Fehler: {e}")
# Hinweis: Dieser Code ist ein einfacher Rabattrechner, der den Endpreis nach Abzug eines Rabatts berechnet.
