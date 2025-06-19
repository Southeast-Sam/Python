# Passwort-Check
def is_passwort_sicher(passwort):
    sonderzeichen = "!@#$%^&*()"

    if len(passwort) < 8:
        return "Zu kurz: Mindestens 8 Zeichen."
    
    if not any(c.isupper() for c in passwort):
        return "Fehlt: Großbuchstabe."
    
    if not any(c.isdigit() for c in passwort):
        return "Fehlt: Zahl."
    
    if not any(c in sonderzeichen for c in passwort):
        return "Fehlt: Sonderzeichen."
    
    return "✅ Dein Passwort ist sicher!"

pw = input("Gib dein Passwort ein: ")
print(is_passwort_sicher(pw))