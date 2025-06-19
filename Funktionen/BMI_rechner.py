# BMI-Rechner
def bmi_rechner(gewicht, groesse):
    bmi = gewicht / (groesse ** 2)
    bmi = round(bmi, 2)
    if bmi < 18.5:
        kategorie = "Untergewicht"
    elif bmi < 25:
        kategorie = "Normalgewicht"
    elif bmi < 30:
        kategorie = "Übergewicht"
    else:
        kategorie = "Fettleibigkeit"
    return f"Dein BMI ist {bmi} - {kategorie}"
    
print(bmi_rechner(70, 1.75))