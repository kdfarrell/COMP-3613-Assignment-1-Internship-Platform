from App.database import db
from App.models.shortlist_entry import ShortlistEntry

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    staff_name = db.Column(db.String(100), nullable=False)

    # One staff member can create many shortlist entries
    shortlists = db.relationship("ShortlistEntry", backref="staff", lazy=True)

    def __init__(self, staff_name):
        self.staff_name = staff_name

    def get_json(self):
        return {
            'staff_id': self.staff_id,
            'name': self.staff_name
        }
    
    # --- Methods ---
    def add_to_shortlist(self, position_id, student_id):
        entry = ShortlistEntry(position_id=position_id, student_id=student_id, staff_id=self.staff_id)
        db.session.add(entry)
        db.session.commit()
        return entry