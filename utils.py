import json

def daten_speichern(dateiname, daten):
    with open(dateiname, 'w') as f:
        json.dump(daten, f)

def daten_laden(dateiname):
    with open(dateiname, 'r') as f:
        return json.load(f)
