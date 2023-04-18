from ast import Pass
from contextlib import redirect_stderr
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import os
import correo
import algoritmo

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(["txt"])

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    else :
        return False

@app.route('/Encriptado',methods=['POST'])
def upload():
    Correo = request.form["correo"]
    print(Correo)
    file = request.files["uploadFile"]
    filename = secure_filename(file.filename)
    print(file)
    print(filename)
    if file and allowed_file(filename):
        print("PERMITIDO")
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        correo.EnviarCorreo(filename, Correo)
        return index()

@app.route('/Desencriptado',methods=['POST'])
def download():
    file = request.files["uploadFile2"]
    Codigo1 = request.form["numero3"]
    Codigo2 = request.form["numero4"]
    print(file)
    print(Codigo1,Codigo2)
    filename2 = secure_filename(file.filename)
    print(filename2)
    if file and allowed_file(filename2):
        print("PERMITIDO")
        file.save(os.path.join(app.config["UPLOAD_FOLDER2"],filename2))
        algoritmo.Desencriptar(filename2, Codigo1, Codigo2)
    return index()

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.config["UPLOAD_FOLDER"] = "static/Encriptado/"
    app.config["UPLOAD_FOLDER2"] = "static/Desencriptado/"
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
