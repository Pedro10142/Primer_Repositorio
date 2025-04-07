from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola_mundo():
    return "Hola mundo" 

@app.route('/')
def hola_mundo2():
    return "Hola mundo 2" 

if __name__ == "__main__":
    app.run(debug=True)