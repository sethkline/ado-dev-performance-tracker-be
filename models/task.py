from .base_model import db, BaseModel

class Task(BaseModel):
    __tablename__ = 'tasks'

    title = db.Column(db.String(100), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'), nullable=False)
    goal = db.relationship('Goal', back_populates='tasks')
