from App.database import db
from App.models.internship_position import InternshipPosition
from App.models.shortlist_entry import ShortlistEntry

class Employer(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)

    # One employer can post many internship positions
    positions = db.relationship("InternshipPosition", backref="employer", lazy=True)

    def __init__(self, emp_name, company_name):
        self.emp_name = emp_name
        self.company_name = company_name
    
    def get_json(self):
        return {
            'emp_id': self.emp_id,
            'emp_name': self.emp_name,
            'company_name': self.company_name
        }
    
    # --- Methods ---

    def create_position(self, position_title, position_description="No description provided"):
        position = InternshipPosition(
            position_title=position_title,
            emp_id=self.emp_id,
            position_description=position_description
        )
        db.session.add(position)
        db.session.commit()
        return position
    
    def respond_to_shortlist(self, entry_id, new_status):
        entry = ShortlistEntry.query.get(entry_id)
        if entry and entry.position.emp_id == self.emp_id:
            entry.status = new_status
            db.session.commit()
            return entry
        return None