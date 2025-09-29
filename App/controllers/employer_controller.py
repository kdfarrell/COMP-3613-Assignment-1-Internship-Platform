from App.models import Employer
from App.database import db

class EmployerController:

    def create_position(self, emp_id, title, description=""):
        employer = Employer.query.get(emp_id)
        if not employer:
            return "\n❌ Employer not found."

        position = employer.create_position(position_title=title)
        position.position_description = description
        db.session.commit()

        output = (
            f"\n✅ Position created successfully!\n"
            f"Created by: {employer.emp_name}\n"
            f"Company: {employer.company_name}\n"
            f"Position Title: {position.position_title}\n"
            f"Description: {position.position_description}"
        )
        return output

    def respond_to_shortlist(self, emp_id, entry_id, new_status):
        if new_status not in ["pending", "accepted", "rejected"]:
            return "\n❌ Invalid status. Must be 'pending', 'accepted', or 'rejected'."

        employer = Employer.query.get(emp_id)
        if not employer:
            return "\n❌ Employer not found."
        
        entry = employer.respond_to_shortlist(entry_id, new_status)
        if not entry:
            return "\n❌ Shortlist entry not found or not authorized."

        output = (
            f"\n✅ Shortlist updated successfully!\n"
            f"Created by: {entry.position.employer.emp_name}\n"
            f"Company: {entry.position.employer.company_name}\n"
            f"Position Title: {entry.position.position_title}\n"
            f"Description: {entry.position.position_description}\n"
            f"Candidate: {entry.student.student_name}\n"
            f"Status: {entry.status}"
        )
        return output
