from app import app, db
from flask import render_template, request, session, redirect, url_for, flash
from app.models import Data

@app.route('/')
def index():
    all_data = Data.query.all()

    return render_template('index.html', all_data = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        x = Data(name=name,email=email,phone=phone)
        db.session.add(x)
        db.session.commit()

        flash('It was added with success','success')

        return redirect(url_for('index'))

    