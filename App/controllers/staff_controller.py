from App.models import Staff, Student, InternshipPosition, ShortlistEntry
from App.database import db

class StaffController:

    def add_to_shortlist(self, staff_id, student_id, position_id):
        staff = Staff.query.get(staff_id)
        student = Student.query.get(student_id)
        position = InternshipPosition.query.get(position_id)

        if not staff:
            return "\n❌ Staff not found."
        if not student:
            return "\n❌ Student not found."
        if not position:
            return "\n❌ Position not found."

        
        existing = ShortlistEntry.query.filter_by(
            staff_id=staff_id,
            student_id=student_id,
            position_id=position_id
        ).first()
        if existing:
            return "\n❌ This student is already shortlisted for this position."

        entry = staff.add_to_shortlist(position_id=position_id, student_id=student_id)

        output = (
            f"\n✅ Student added to shortlist!\n"
            f"Student Name: {student.student_name}\n"
            f"Position Title: {position.position_title}\n"
            f"Company: {position.employer.company_name}\n"
            f"Description: {position.position_description}"
        )
        return output
