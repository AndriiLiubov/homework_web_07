from sqlalchemy import func, desc, select, and_

from conf.models import Group, Student, Teacher, Subject, Grade
from conf.db import session

def select_1():

    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_2():

    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subjects_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result

def select_3():
    result = (
        session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(desc('average_grade'))
        .limit(5)
        .all()
    )
    return result

def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).scalar()
    return result

def select_5():
    result = (
            session.query(Teacher.fullname.label('teacher_name'), Subject.name.label('course_name'))
            .join(Subject, Teacher.id == Subject.teacher_id)
            .all()
        )
    return result

def select_6(group_name):
    result = (
        session.query(Student.fullname.label('student_name'))
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .all()
    )
    return result

def select_7(group_name, subject_name):
    result = (
        session.query(Student.fullname.label('student_name'), Grade.grade.label('grade'))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subjects_id == Subject.id)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .filter(Subject.name == subject_name)
        .all()
    )
    return result

def select_8(teacher_name):
    result = (
            session.query(func.round(func.avg(Grade.grade), 2).label('average_grade'))
            .join(Subject, Teacher.id == Subject.teacher_id)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .filter(Teacher.fullname == teacher_name)
            .scalar()
    )
    return result

def select_9(student_name):
    result = (
            session.query(Subject.name.label('course_name'))
            .join(Grade, Subject.id == Grade.subjects_id)
            .join(Student, Student.id == Grade.student_id)
            .filter(Student.fullname == student_name)
            .all()
        )
    return result

def select_10(teacher_name, student_name):
    result = (
            session.query(Subject.name.label('course_name'))
            .join(Grade, Subject.id == Grade.subjects_id)
            .join(Student, Student.id == Grade.student_id)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .filter(Student.fullname == student_name)
            .filter(Teacher.fullname == teacher_name)
            .all()
        )
    return result


if __name__ == '__main__':
    # print(select_1())
    # print(select_2())
    # print(select_3())
    # print(select_4())
    # print(select_5())
    # print(select_6("Group C"))
    # print(select_7("Group B", "Algebra"))
    # print(select_8("Еріка Чумак"))
    # print(select_9("Демʼян Царенко"))
    print(select_10("Еріка Чумак", "Демʼян Царенко"))