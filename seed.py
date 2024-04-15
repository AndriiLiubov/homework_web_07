import random
from datetime import datetime, timedelta

from faker import Faker

from conf.models import Group, Student, Teacher, Subject, Grade
from conf.db import session


fake = Faker(locale="uk-UA")

def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))


def populate_groups():
    groups = ["Group A", "Group B", "Group C"]
    for group_name in groups:
        group = Group(name=group_name)
        session.add(group)
    session.commit()


def populate_students(num_students):
    for _ in range(num_students):
        fullname = fake.name()
        group_id = random.randint(1, 3)
        student = Student(fullname=fullname, group_id=group_id)
        session.add(student)
    session.commit()


def populate_teachers(num_teachers):
    for _ in range(num_teachers):
        fullname = fake.name()
        teacher = Teacher(fullname=fullname)
        session.add(teacher)
    session.commit()


def populate_subjects(num_subjects):
    subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Literature", "Geography", "English", "Geometry", "Algebra", "Drawing"]
    for _ in range(num_subjects):
        name = random.choice(subjects)
        teacher_id = random.randint(1, 3)
        subject = Subject(name=name, teacher_id=teacher_id)
        session.add(subject)
    session.commit()


def populate_grades(num_grades):
    start_date = datetime(2023, 9, 1)
    end_date = datetime.now()
    for _ in range(num_grades):
        student_id = random.randint(1, 30)  
        subject_id = random.randint(1, 8)  
        grade = random.randint(0, 100)  
        grade_date = random_date(start_date, end_date)
        grade_entry = Grade(student_id=student_id, subjects_id=subject_id, grade=grade, grade_date=grade_date)
        session.add(grade_entry)
    session.commit()

if __name__ == "__main__":
    populate_groups()
    populate_students(50)  
    populate_teachers(5)   
    populate_subjects(10)  
    populate_grades(1000)