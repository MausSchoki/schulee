from benutzerverwaltung import Benutzerverwaltung
from schuelerverwaltung import SchuelerVerwaltung
from lehrerverwaltung import LehrerVerwaltung
from klassenverwaltung import KlassenVerwaltung
from stundenplan import Stundenplan
from kommunikation import Kommunikation

def main():
    print("Willkommen im Schulmanager!")
    benutzerverwaltung = Benutzerverwaltung()
    schuelerverwaltung = SchuelerVerwaltung()
    lehrerverwaltung = LehrerVerwaltung()
    klassenverwaltung = KlassenVerwaltung()
    stundenplan = Stundenplan()
    kommunikation = Kommunikation()

    # Beispielaktionen
    benutzerverwaltung.benutzer_hinzufuegen("Jannik", "Admin", "pass123")
    lehrerverwaltung.lehrer_hinzufuegen("Herr Müller", "Mathematik")
    schuelerverwaltung.schueler_hinzufuegen("Marie", "7B")
    klassenverwaltung.klasse_erstellen("7B")

    print("\nSetup abgeschlossen! Wähle eine Aktion im Menü.")

if __name__ == "__main__":
    main()
