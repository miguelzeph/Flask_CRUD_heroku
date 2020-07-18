from app import app
from flask import render_template, request, session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods = ['POST','GET'])
def enviar():
    if request.method == 'POST':
        print('oi')
        print(request.form["name"])
    return render_template('index.html')