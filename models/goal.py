from .base_model import db, BaseModel

class Goal(BaseModel):
    __tablename__ = 'goals'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tasks = db.relationship('Task', back_populates='goal', lazy='dynamic')
