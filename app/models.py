from app import db

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tenantname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    db.relationship('MetersReader', backref = 'tenant', lazy = 'dynamic')

    def __repr__(self):
        return f'<Tenant {self.tenantname}>'

class MetersReader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    cold_water = db.Column(db.Float)
    hot_water = db.Column(db.Float)
    electricity = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('tenant.id'))

    def __repr__(self):
        return f'On {self.date} was used:\n{self.hot_water}\n{self.cold_water}\n{self.electricity}'

