class Lehrer:
    def __init__(self, name, fach):
        self.name = name
        self.fach = fach

class LehrerVerwaltung:
    def __init__(self):
        self.lehrer_liste = []

    def lehrer_hinzufuegen(self, name, fach):
        neuer_lehrer = Lehrer(name, fach)
        self.lehrer_liste.append(neuer_lehrer)

    def lehrer_anzeigen(self):
        for lehrer in self.lehrer_liste:
            print(f"Lehrer: {lehrer.name}, Fach: {lehrer.fach}")
