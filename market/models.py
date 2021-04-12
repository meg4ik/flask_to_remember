from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), nullable=False,unique=True)
    email_adress = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable = False,default=1000)
    items = db.relationship('Item', backref='owner_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >=4:
            return "{},{}".format(str(self.budget)[:-3], str(self.budget)[-3:])+ "$" 
        else:
            return str(self.budget) + "$" 

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text):
        self.password_hash = bcrypt.generate_password_hash(plain_text).decode('utf-8')

    def check_password_correction(self, attemp_pass):
        return bcrypt.check_password_hash(self.password_hash, attemp_pass)
        


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return "Item {}".format(self.name)