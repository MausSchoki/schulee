from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Willkommen im Schulmanager!"

if __name__ == '__main__':
    app.run(debug=True)
