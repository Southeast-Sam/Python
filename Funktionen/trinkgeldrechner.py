def trinkgeld_rechner(betrag, prozent):
    trinkgeld = betrag * (prozent / 100)
    gesamtbetrag = betrag + trinkgeld
    gesamtbetrag = round(gesamtbetrag, 2)
    return f"Gesamtbetrag: {gesamtbetrag:.2f}€ (inkl. {prozent}% Trinkgeld)"

betrag = float(input("Gib den Rechnungsbetrag ein (in €): "))
prozent = float(input("Wie viel Prozent Trinkgeld möchtest du geben?: "))
print(trinkgeld_rechner(betrag, prozent))