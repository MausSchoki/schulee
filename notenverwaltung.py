class NotenVerwaltung:
    def __init__(self):
        self.noten_liste = {}

    def note_hinzufuegen(self, schueler, note):
        if schueler not in self.noten_liste:
            self.noten_liste[schueler] = []
        self.noten_liste[schueler].append(note)

    def durchschnitt_berechnen(self, schueler):
        noten = self.noten_liste.get(schueler, [])
        return sum(noten) / len(noten) if noten else 0
