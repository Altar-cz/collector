from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Server bezi!", 200

@app.route('/upload', methods=['POST'])
def upload():
    # Render nepovoli trvale ukladani, takze soubor jen "prijmeme" 
    # a vypiseme jeho nazev do logu pro overeni.
    if 'file' in request.files:
        f = request.files['file']
        print(f"[*] Prijat soubor: {f.filename}")
        # Docasne ulozeni (v Renderu po case zmizi)
        f.save(f.filename) 
        return f"Prijato: {f.filename}", 200
    return "Zadny soubor", 400

if __name__ == '__main__':
    # Port musi byt dynamicky pro Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
