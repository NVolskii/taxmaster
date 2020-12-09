from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(120))
    second_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    is_tenant = db.Column(db.Boolean)
    is_landlord = db.Column(db.Boolean)
    db.relationship('Meter', backref='tenant', lazy='dynamic')
    db.relationship('Meter', backref='landlord', lazy='dynamic')

    def __repr__(self):
        return f'<User id: {self.id}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Meter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    landlord_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    db.relationship('MeterReading', backref='meter', lazy='dynamic')
    db.relationship('MeterTax', backref='meter', lazy='dynamic')

    def __repr__(self):
        return f'MetersReader id: {self.id}'

class MeterReading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meter.id'))
    input_date = db.Column(db.Date)
    reading = db.Column(db.Float)


class MeterTax(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meter.id'))
    tax_rate = db.Column(db.Float)
    valid_from = db.Column(db.Date)
    valid_until = db.Column(db.Date)

    def __repr__(self):
        return f'TaxRate id: {self.id}'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))