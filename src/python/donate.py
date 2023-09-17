"""Geting Flask"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def defaulthome():
    """Homepage"""
    return render_template('home.html')

@app.route('/home')
def home():
    """Rendering index.html"""
    return render_template('home.html')

@app.route('/form')

def form():
    """Rendering index.html"""
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    """Gathering the request"""
    if request.method == 'POST':
        name = request.form.get("firstname")
        surname= request.form.get('lastname')
        ammount = request.form.get('ammount')
        cont =request.form.get('ammount')
        print(name, ammount)
    return render_template('thanks.html', firstname=name, lastname=surname, cont=cont)

if __name__ == '__main__':
    app.run(debug=True)
# End-of-file (EOF)
