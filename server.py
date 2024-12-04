# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy-Daten (später mit einer Datenbank verbinden)
schueler = [{"name": "Marie", "klasse": "7B", "noten": [1, 2, 3]}]
lehrer = [{"name": "Herr Müller", "fach": "Mathematik"}]

@app.route('/')
def home():
    return "Willkommen im Schulmanager!"

@app.route('/api/schueler', methods=['GET', 'POST'])
def schueler_verwaltung():
    if request.method == 'GET':
        return jsonify(schueler)
    elif request.method == 'POST':
        neuer_schueler = request.json
        schueler.append(neuer_schueler)
        return jsonify({"message": "Schüler hinzugefügt!"}), 201

@app.route('/api/lehrer', methods=['GET'])
def lehrer_verwaltung():
    return jsonify(lehrer)

if __name__ == '__main__':
    app.run(debug=True)
