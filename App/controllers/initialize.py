from .user import create_user
from App.database import db
from App.models import Employer, Student, Staff, InternshipPosition, ShortlistEntry

def initialize():
    # Reset the database
    db.drop_all()
    db.create_all()

    # --- Defualt Internship Platform Data ---

    # Employers
    emp1 = Employer(emp_name="Alice", company_name="TechCorp")
    emp2 = Employer(emp_name="Bob", company_name="DataWorks")
    db.session.add_all([emp1, emp2])

    # Students
    stu1 = Student(student_name="John")
    stu2 = Student(student_name="Jane")
    stu3 = Student(student_name="Mark")  # New student for testing
    db.session.add_all([stu1, stu2, stu3])

    # Staff
    staff1 = Staff(staff_name="Sam")
    staff2 = Staff(staff_name="Sara")
    db.session.add_all([staff1, staff2])

    # Commit to assign IDs
    db.session.commit()

    # Positions
    pos1 = InternshipPosition(position_title="Backend Intern", emp_id=emp1.emp_id, position_description="Work on backend APIs")
    pos2 = InternshipPosition( position_title="Data Analyst", emp_id=emp2.emp_id, position_description="Analyze company data")
    
    db.session.add_all([pos1, pos2])
    db.session.commit()

    # Shortlist Entries
    entry1 = ShortlistEntry(position_id=pos1.position_id, student_id=stu1.student_id, staff_id=staff1.staff_id)
    entry2 = ShortlistEntry(position_id=pos2.position_id, student_id=stu2.student_id, staff_id=staff2.staff_id)
    db.session.add_all([entry1, entry2])
    db.session.commit()
