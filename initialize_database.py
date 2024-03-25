from app import create_app
from extensions import db
# Import all models to ensure SQLAlchemy is aware of them
from models.goal import Goal
from models.task import Task
from models.comment import Comment

app = create_app()
with app.app_context():
    db.create_all()
