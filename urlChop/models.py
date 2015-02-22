from . import db, bcrypt, login_manager
from flask.ext.login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    encrypted_password = db.Column(db.String(60))

    def get_password(self):
        return getattr(self, "_password", None)
        return self._password

    def set_password(self, password):
        self._password = password
        self.encrypted_password = bcrypt.generate_password_hash(password)

    password = property(None, set_password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.encrypted_password, password)

    # @property
    # def all_links(self):
    #     return [links.longlink for links in self.links]

    def __repr__(self):
        return "<User {}>".format(self.email)

# class Links(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     longlink = db.Column(db.String(255), nullable=False)
#     shortlink = db.Column(db.String(255), unique=True, nullable=False)
#     description = db.Column(db.String(255))
#     user = db.relationship('User', backref=db.backref('favorites', lazy='dynamic'))
#
#     def __repr__(self):
#         return "<Links {}>".format(self.email)