from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///UserProfiles.db"
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    profile = db.relationship('Profile', backref='user', uselist=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
def fill_database():



    user = User(username='lol', email='lol')
    profile = Profile(full_name='lol', bio='lol', user_id=user.id)
    db.session.add(user)
    db.session.add(profile)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)