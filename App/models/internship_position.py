from App.database import db

class InternshipPosition(db.Model):
    position_id = db.Column(db.Integer, primary_key=True)
    position_title = db.Column(db.String(150), nullable=False)
    position_description = db.Column(db.String(150), nullable=False)

    # Foreign Key to Employer
    emp_id = db.Column(db.Integer, db.ForeignKey('employer.emp_id'), nullable=False)

    # One Position can have many shortlist entries
    shortlists = db.relationship("ShortlistEntry", backref="position", lazy=True)

    def __init__(self, position_title, emp_id, position_description):
        self.position_title = position_title
        self.emp_id = emp_id
        self.position_description = position_description

    def get_json(self):
       return {
            'position_id': self.position_id,
            'position_title': self.position_title,
            'emp_id': self.emp_id,
            'position_description': self.position_description
        }

