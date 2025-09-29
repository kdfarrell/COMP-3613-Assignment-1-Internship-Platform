import warnings

# Suppress the pkg_resources UserWarning
warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
)

import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# START - INTERNSHIP PLATFORM APP ADDITIONS 

from flask.cli import AppGroup
from App.controllers.employer_controller import EmployerController
from App.controllers.staff_controller import StaffController
from App.controllers.student_controller import StudentController

# Instantiate controllers
employer_ctrl = EmployerController()
staff_ctrl = StaffController()
student_ctrl = StudentController()

internship_cli = AppGroup('internship', help='Internship Platform commands')

# END - INTERNSHIP PLATFORM APP ADDITIONS 



# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('Internship Platform Database Intialized')


# START - INTERNSHIP PLATFORM APP ADDITIONS 

# Employer: create position
@internship_cli.command("create-position", help="Employer creates a position")
@click.argument("emp_id", type=int)
@click.argument("title")
@click.argument("description", default="")
def create_position_command(emp_id, title, description):
    result = employer_ctrl.create_position(emp_id, title, description)
    print(result)

# Employer: respond to shortlist
@internship_cli.command("respond", help="Employer responds to shortlist entry")
@click.argument("emp_id", type=int)
@click.argument("entry_id", type=int)
@click.argument("status")
def respond_command(emp_id, entry_id, status):
    result = employer_ctrl.respond_to_shortlist(emp_id, entry_id, status)
    print(result)

# Staff: add student to shortlist
@internship_cli.command("add-shortlist", help="Staff adds student to shortlist")
@click.argument("staff_id", type=int)
@click.argument("student_id", type=int)
@click.argument("position_id", type=int)
def add_shortlist_command(staff_id, student_id, position_id):
    result = staff_ctrl.add_to_shortlist(staff_id, student_id, position_id)
    print(result)

# Student: view shortlist
@internship_cli.command("view-shortlist", help="Student views their shortlist")
@click.argument("student_id", type=int)
def view_shortlist_command(student_id):
    result = student_ctrl.view_shortlist(student_id)
    print(result)


# END - INTERNSHIP PLATFORM APP ADDITIONS


'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
app.cli.add_command(internship_cli)