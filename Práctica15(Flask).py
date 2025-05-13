from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Pepino" 

# @app.route('/hola') # al cambiar la extension desde aqui se puede acceder a otra ventana distinta (/hola)
# def hola_mundo():
#   return "Hola mundo 2" 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000)
    