class Kommunikation:
    def __init__(self):
        self.nachrichten = []

    def nachricht_senden(self, sender, empfaenger, text):
        nachricht = {"Sender": sender, "Empfänger": empfaenger, "Text": text}
        self.nachrichten.append(nachricht)

    def nachrichten_anzeigen(self):
        for n in self.nachrichten:
            print(f"Von: {n['Sender']} An: {n['Empfänger']} - {n['Text']}")
