from app import db

class Data(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)

    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Nome: {self.name} Email: {self.email} Phone: {self.phone}"