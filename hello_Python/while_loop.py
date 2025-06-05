"""
# Zählen bis 5 mit while
x = 0
while x <= 5:
    print(x)
    x += 1
"""
"""
# 2. Countdown mit while
x = 10
while x > 0:
    print(x)
    x -= 1
    
print("Start!")
"""

"""
# 3. Passwortschutz mit while
password = "geheim"
anzahl_versuche = 0
while anzahl_versuche < 3:
    eingabe = input("Bitte Passwort eingeben: ")
    if eingabe == password:
        print("Zugriff gewährt!")
        break
    else:
        anzahl_versuche += 1
        print(f"Falsches Passwort! Du hast noch {3 - anzahl_versuche} Versuche übrig.")
        if anzahl_versuche == 3:
            print("Zugriff verweigert! Zu viele falsche Versuche.")
"""

name = "brudi"
name.upper()