from app import app, db
from flask import render_template, request, session, redirect, url_for, flash
from app.models import Data

@app.route('/')
def index():
    all_data = Data.query.all()# READ

    return render_template('index.html', all_data = all_data)

@app.route('/create', methods = ['POST'])
def create():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        x = Data(name=name,email=email,phone=phone)
        db.session.add(x)
        db.session.commit()

        flash('It was added with success','success')

        return redirect(url_for('index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':

        my_data = Data.query.get(request.form['id'])
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Employee Updated Successfully", 'success')
 
        return redirect(url_for('index'))

@app.route('/delete/<id>', methods = ['GET','POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully",'success')
 
    return redirect(url_for('index'))