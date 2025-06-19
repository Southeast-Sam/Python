"""# Begrüßungs-funktion
def begruesse(name):
    return f"Hallo {name}, schön dich zu sehen!"

name = begruesse(input("Gib dein Name ein: "))
print(name)"""

# Gerade oder ungerade

def gerade_oder_ungerade(zahl):
    if zahl % 2 != 0:
        return f"{zahl} ist ungerade"
    else:
        return f"{zahl} ist gerade"

ergebnis = gerade_oder_ungerade(int(input("Gib eine Zahl ein: ")))
print(ergebnis)
