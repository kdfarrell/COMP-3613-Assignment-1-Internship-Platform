from App.database import db

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    shortlists = db.relationship("ShortlistEntry", backref="student", lazy=True)

    def __init__(self, student_name):
        self.student_name = student_name

    def get_json(self):
        return {
            'student_id': self.student_id,
            'student_name': self.student_name
        }

    # --- Methods ---
    
    def view_shortlist(self):
        # Returns SQLAlchemy objects, not JSON
        return self.shortlists
