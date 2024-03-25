from .base_model import db, BaseModel

class Post(BaseModel):
    __tablename__ = 'posts'

    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # The 'backref' in the User model's posts relationship will automatically add an 'author' attribute to Post instances
