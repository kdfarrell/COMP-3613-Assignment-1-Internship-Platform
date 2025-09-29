from App.models import Student
from App.database import db


class StudentController:
    
    def view_shortlist(self, student_id, as_json=False):
        student = Student.query.get(student_id)
        if not student:
            return {"error": "Student not found"} if as_json else "\n❌ Student not found."

        entries = student.view_shortlist()
        if not entries:
            return {"student_name": student.student_name, "shortlist": []} if as_json \
                   else f"\nStudent Name: {student.student_name}\nNo shortlisted positions available."

        if as_json:
            return {
                "student_name": student.student_name,
                "shortlist": [entry.get_json() for entry in entries]
            }
        else:
            output_lines = [f"\nShortlist for Student: {student.student_name}"]
            for entry in entries:
                position = entry.position
                output_lines.append(
                    f"\nPosition Title: {position.position_title}\n"
                    f"Company: {position.employer.company_name}\n"
                    f"Description: {position.position_description}\n"
                    f"Status: {entry.status}"
                )
            return "\n".join(output_lines)
