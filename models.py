from extensions import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    group = db.Column(db.String(20), nullable=False)
    course = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.String(20), unique=True)
    admission_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    birth_date = db.Column(db.Date)
    performance = db.Column(db.Float)
    notes = db.Column(db.Text)
    photo_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    courses = db.relationship('Course', secondary='student_course', back_populates='students')
    
    def __repr__(self):
        return f'<Student {self.last_name} {self.first_name}>'