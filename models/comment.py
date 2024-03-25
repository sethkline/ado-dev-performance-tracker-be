from .base_model import db, BaseModel

class Comment(BaseModel):
    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    task = db.relationship('Task', backref=db.backref('comments', lazy=True))
