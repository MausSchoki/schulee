class Benutzer:
    def __init__(self, name, rolle, passwort):
        self.name = name
        self.rolle = rolle  # Rollen: Admin, Lehrer, Schüler
        self.passwort = passwort

class Benutzerverwaltung:
    def __init__(self):
        self.benutzerliste = []

    def benutzer_hinzufuegen(self, name, rolle, passwort):
        neuer_benutzer = Benutzer(name, rolle, passwort)
        self.benutzerliste.append(neuer_benutzer)

    def login(self, name, passwort):
        for benutzer in self.benutzerliste:
            if benutzer.name == name and benutzer.passwort == passwort:
                print(f"Login erfolgreich! Willkommen, {benutzer.name} ({benutzer.rolle}).")
                return benutzer
        print("Login fehlgeschlagen.")
        return None
