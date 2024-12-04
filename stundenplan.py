class Stundenplan:
    def __init__(self):
        self.plan = {}

    def stunde_hinzufuegen(self, tag, stunde, fach, lehrer):
        if tag not in self.plan:
            self.plan[tag] = {}
        self.plan[tag][stunde] = {"Fach": fach, "Lehrer": lehrer}

    def anzeigen(self):
        for tag, stunden in self.plan.items():
            print(f"{tag}:")
            for stunde, details in stunden.items():
                print(f"  Stunde {stunde}: {details['Fach']} mit {details['Lehrer']}")
