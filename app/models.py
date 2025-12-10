from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=Fals)
    status = db.Column(db.String(20), deafult="Pending")