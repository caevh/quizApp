from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    hash_password = db.Column(db.String(120))

    def __repr__(self):
        return f'<user {self.username}>'
    
    def set_password(self, password):
        """
        Used on Registration:
        Takes users password and generates a hash.
        """
        self.hash_password = generate_password_hash(password)
    
    def password_verify(self, password):
        """
        Used on Login:
        Used to verify users password against the hashed alternative
        Retruns: Boolean 
        """
        return check_password_hash(self.hash_password, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
