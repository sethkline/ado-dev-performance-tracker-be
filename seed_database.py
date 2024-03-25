from app import create_app
from extensions import db
from models.goal import Goal  # Ensure correct import paths
from models.task import Task
from models.comment import Comment

def seed_data():
    # Your seeding logic remains the same
    goal1 = Goal(title='Learn Flask', description='Understand Flask basics')
    # Assuming you've fixed the model relationships and foreign key issues:
    db.session.add(goal1)
    db.session.commit()  # Commit to ensure goal1 has an ID before using it in relationships

    task1 = Task(title='Read Flask Documentation', goal_id=goal1.id)
    comment1 = Comment(content='This is a comment on the first task.', task_id=task1.id)

    db.session.add(task1)
    db.session.add(comment1)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        seed_data()