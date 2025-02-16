from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, PrimaryKeyConstraint

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id', ondelete='SET NULL'))
    teacher = db.relationship('Teacher', backref='students', lazy=True)
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"


class Course(db.Model):
    __tablename__ = 'courses'

    course_code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

    def __repr__(self):
        return f"<Course(code='{self.course_code}', name='{self.name}')>"


class Semester(db.Model):
    __tablename__ = 'semesters'

    year = db.Column(db.Integer, nullable=False)
    term = db.Column(db.Integer, nullable=False)

    enrollments = db.relationship('Enrollment', backref='semester', lazy=True)

    __table_args__ = (
        db.CheckConstraint('term IN (1, 2)', name='valid_term'),
        db.UniqueConstraint('year', 'term', name='unique_semester'),
        PrimaryKeyConstraint('year', 'term')
    )

    def __repr__(self):
        return f"<Semester(year={self.year}, term={self.term})>"


GRADE_OPTIONS = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "D+", "D", "F")

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    course_code = db.Column(db.String(20), db.ForeignKey('courses.course_code', ondelete='CASCADE'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    term = db.Column(db.Integer, nullable=False)
    grade = db.Column(Enum(*GRADE_OPTIONS, name="grade_enum"), nullable=False)
    gpa = db.Column(db.Numeric(3, 2), nullable=False)

    __table_args__ = (
        db.ForeignKeyConstraint(['year', 'term'], ['semesters.year', 'semesters.term'], ondelete='CASCADE'),
        db.CheckConstraint('gpa >= 0.0 AND gpa <= 5.0', name='valid_gpa'),
        db.UniqueConstraint('student_id', 'course_code', 'year', 'term', name='unique_enrollment'),
    )

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_code='{self.course_code}', year={self.year}, term={self.term})>"
    
