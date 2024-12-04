class Klasse:
    def __init__(self, name):
        self.name = name
        self.schueler = []

    def schueler_hinzufuegen(self, schueler):
        self.schueler.append(schueler)

class KlassenVerwaltung:
    def __init__(self):
        self.klassen_liste = []

    def klasse_erstellen(self, name):
        neue_klasse = Klasse(name)
        self.klassen_liste.append(neue_klasse)

    def klassen_anzeigen(self):
        for klasse in self.klassen_liste:
            print(f"Klasse: {klasse.name}, Schüleranzahl: {len(klasse.schueler)}")
