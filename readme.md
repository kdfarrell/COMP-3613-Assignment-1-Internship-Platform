# Internship Platform Application

A guide to all CLI commands for the Internship Platform project.

---

## Setup

```sh
pip install -r requirements.txt
flask init
```

This will install dependencies and initialize the database with default test data.

---

## Command Overview

### Employer Commands

- `flask internship create-position <emp_id> <title> [description]`  
   Add a new internship position.

- `flask internship respond <emp_id> <entry_id> <status>`  
  Update a student’s shortlist status (`pending`, `accepted`, `rejected`).

### Staff Commands

- `flask internship add-shortlist <staff_id> <student_id> <position_id>`  
  Add a student to a position’s shortlist.

### Student Commands

- `flask internship view-shortlist <student_id>`  
  See all positions a student is shortlisted for.

---

## Test Data

**Employers**
```sh
flask internship create-position 1 "Frontend Intern" "Work on React applications"
flask internship respond 2 2 accepted
```

**Staff**
```sh
flask internship add-shortlist 1 3 1
```

**Students**
```sh
flask internship view-shortlist 3
```

---

