class Schueler:
    def __init__(self, name, klasse):
        self.name = name
        self.klasse = klasse
        self.noten = []

    def noten_hinzufuegen(self, note):
        self.noten.append(note)

    def durchschnitt(self):
        return sum(self.noten) / len(self.noten) if self.noten else 0

class SchuelerVerwaltung:
    def __init__(self):
        self.schueler_liste = []

    def schueler_hinzufuegen(self, name, klasse):
        neuer_schueler = Schueler(name, klasse)
        self.schueler_liste.append(neuer_schueler)

    def schueler_anzeigen(self):
        for s in self.schueler_liste:
            print(f"Name: {s.name}, Klasse: {s.klasse}, Durchschnitt: {s.durchschnitt():.2f}")
