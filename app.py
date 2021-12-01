from flask import Flask,render_template
#from flask import render_template

app = Flask(__name__)


@app.route('/')
def homesite():
    return render_template('homesite.html')

@app.route('/Home')
def Homesite():
    return ('homesite.html')

@app.route('/Sobre')
def sobre1():
    return render_template('sobre1.html')

@app.route('/Projetos')
def Projetos1():
    return render_template('Projetos1.html')

@app.route('/Contato')
def Contato():
    return render_template('contato.html')

from app import app

if __name__ == "__main__":
    app.run(debug=True)



