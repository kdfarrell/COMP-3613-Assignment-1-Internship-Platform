from App.database import db

class ShortlistEntry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Foreign keys
    position_id = db.Column(db.Integer, db.ForeignKey('internship_position.position_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)

    # Status: pending, accepted, rejected
    status = db.Column(db.String(20), default="pending")

    def __init__(self, position_id, student_id, staff_id, status="pending"):
        self.position_id = position_id
        self.student_id = student_id
        self.staff_id = staff_id
        self.status = status

    def get_json(self):
        return {
            'entry_id': self.entry_id,
            'position_id': self.position_id,
            'student_id': self.student_id,
            'staff_id': self.staff_id,
            'status': self.status
        }

    # --- Methods ---
    
    def update_status(self, new_status):
        self.status = new_status
