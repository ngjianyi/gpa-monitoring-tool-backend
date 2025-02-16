from app import create_app, db
from models.models import Student, Teacher, Course, Semester, Enrollment

app = create_app()

GRADE_TO_GPA = {
    "A+": 5.0, "A": 5.0, "A-": 4.5, "B+": 4.0, "B": 3.5, 
    "B-": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0
}

with app.app_context():
    # Reset the database
    db.drop_all()
    db.create_all()

    # Create Teachers
    teacher1 = Teacher(name="Dr. Alice")
    teacher2 = Teacher(name="Dr. Bob")
    db.session.add(teacher1)
    db.session.add(teacher2)
    db.session.commit()

    # Create Students
    student1 = Student(name="Student 1", teacher_id=teacher1.id)
    student2 = Student(name="Student 2", teacher_id=teacher1.id)
    student3 = Student(name="Student 3", teacher_id=teacher1.id)
    student4 = Student(name="Student 4", teacher_id=teacher1.id)
    student5 = Student(name="Student 5", teacher_id=teacher1.id)

    student6 = Student(name="Student 6", teacher_id=teacher2.id)
    student7 = Student(name="Student 7", teacher_id=teacher2.id)
    student8 = Student(name="Student 8", teacher_id=teacher2.id)
    student9 = Student(name="Student 9", teacher_id=teacher2.id)
    student10 = Student(name="Student 10", teacher_id=teacher2.id)

    db.session.add_all([student1, student2, student3, student4, student5,
                        student6, student7, student8, student9, student10])
    db.session.commit()

    # Create Semesters (8 semesters over 4 years)
    semester1 = Semester(year=2021, term=1)
    semester2 = Semester(year=2021, term=2)
    semester3 = Semester(year=2022, term=1)
    semester4 = Semester(year=2022, term=2)
    semester5 = Semester(year=2023, term=1)
    semester6 = Semester(year=2023, term=2)
    semester7 = Semester(year=2024, term=1)
    semester8 = Semester(year=2024, term=2)

    db.session.add_all([semester1, semester2, semester3, semester4, semester5,
                        semester6, semester7, semester8])
    db.session.commit()

    # Create Courses
    course1 = Course(course_code="COURSE1", name="Course 1")
    course2 = Course(course_code="COURSE2", name="Course 2")
    course3 = Course(course_code="COURSE3", name="Course 3")
    course4 = Course(course_code="COURSE4", name="Course 4")
    course5 = Course(course_code="COURSE5", name="Course 5")
    course6 = Course(course_code="COURSE6", name="Course 6")
    course7 = Course(course_code="COURSE7", name="Course 7")
    course8 = Course(course_code="COURSE8", name="Course 8")

    db.session.add_all([course1, course2, course3, course4, course5, course6, course7, course8])
    db.session.commit()

    # Enroll all students in the corresponding course for each semester
    # Semester 1 - Course 1
    enrollment1 = Enrollment(student_id=student1.id, course_code=course1.course_code, year=semester1.year, term=semester1.term,
                             grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment2 = Enrollment(student_id=student2.id, course_code=course1.course_code, year=semester1.year, term=semester1.term,
                             grade="A-", gpa=GRADE_TO_GPA["A-"])
    enrollment3 = Enrollment(student_id=student3.id, course_code=course1.course_code, year=semester1.year, term=semester1.term,
                             grade="B+", gpa=GRADE_TO_GPA["B+"])
    enrollment4 = Enrollment(student_id=student4.id, course_code=course1.course_code, year=semester1.year, term=semester1.term,
                             grade="B", gpa=GRADE_TO_GPA["B"])
    enrollment5 = Enrollment(student_id=student5.id, course_code=course1.course_code, year=semester1.year, term=semester1.term,
                             grade="C", gpa=GRADE_TO_GPA["C"])

    # Semester 2 - Course 2
    enrollment6 = Enrollment(student_id=student6.id, course_code=course2.course_code, year=semester2.year, term=semester2.term,
                             grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment7 = Enrollment(student_id=student7.id, course_code=course2.course_code, year=semester2.year, term=semester2.term,
                             grade="B+", gpa=GRADE_TO_GPA["B+"])
    enrollment8 = Enrollment(student_id=student8.id, course_code=course2.course_code, year=semester2.year, term=semester2.term,
                             grade="B", gpa=GRADE_TO_GPA["B"])
    enrollment9 = Enrollment(student_id=student9.id, course_code=course2.course_code, year=semester2.year, term=semester2.term,
                             grade="C+", gpa=GRADE_TO_GPA["C+"])
    enrollment10 = Enrollment(student_id=student10.id, course_code=course2.course_code, year=semester2.year, term=semester2.term,
                              grade="D+", gpa=GRADE_TO_GPA["D+"])

    # Semester 3 - Course 3
    enrollment11 = Enrollment(student_id=student1.id, course_code=course3.course_code, year=semester3.year, term=semester3.term,
                              grade="A-", gpa=GRADE_TO_GPA["A-"])
    enrollment12 = Enrollment(student_id=student2.id, course_code=course3.course_code, year=semester3.year, term=semester3.term,
                              grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment13 = Enrollment(student_id=student3.id, course_code=course3.course_code, year=semester3.year, term=semester3.term,
                              grade="B", gpa=GRADE_TO_GPA["B"])
    enrollment14 = Enrollment(student_id=student4.id, course_code=course3.course_code, year=semester3.year, term=semester3.term,
                              grade="C+", gpa=GRADE_TO_GPA["C+"])
    enrollment15 = Enrollment(student_id=student5.id, course_code=course3.course_code, year=semester3.year, term=semester3.term,
                              grade="D", gpa=GRADE_TO_GPA["D"])

    # Semester 4 - Course 4
    enrollment16 = Enrollment(student_id=student6.id, course_code=course4.course_code, year=semester4.year, term=semester4.term,
                              grade="B-", gpa=GRADE_TO_GPA["B-"])
    enrollment17 = Enrollment(student_id=student7.id, course_code=course4.course_code, year=semester4.year, term=semester4.term,
                              grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment18 = Enrollment(student_id=student8.id, course_code=course4.course_code, year=semester4.year, term=semester4.term,
                              grade="A-", gpa=GRADE_TO_GPA["A-"])
    enrollment19 = Enrollment(student_id=student9.id, course_code=course4.course_code, year=semester4.year, term=semester4.term,
                              grade="B+", gpa=GRADE_TO_GPA["B+"])
    enrollment20 = Enrollment(student_id=student10.id, course_code=course4.course_code, year=semester4.year, term=semester4.term,
                              grade="C", gpa=GRADE_TO_GPA["C"])
    
    # Semester 5 - Course 5
    enrollment21 = Enrollment(student_id=student1.id, course_code=course5.course_code, year=semester5.year, term=semester5.term,
                              grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment22 = Enrollment(student_id=student2.id, course_code=course5.course_code, year=semester5.year, term=semester5.term,
                              grade="B+", gpa=GRADE_TO_GPA["B+"])
    enrollment23 = Enrollment(student_id=student3.id, course_code=course5.course_code, year=semester5.year, term=semester5.term,
                              grade="B", gpa=GRADE_TO_GPA["B"])
    enrollment24 = Enrollment(student_id=student4.id, course_code=course5.course_code, year=semester5.year, term=semester5.term,
                              grade="B-", gpa=GRADE_TO_GPA["B-"])
    enrollment25 = Enrollment(student_id=student5.id, course_code=course5.course_code, year=semester5.year, term=semester5.term,
                              grade="C", gpa=GRADE_TO_GPA["C"])

    # Semester 6 - Course 6
    enrollment26 = Enrollment(student_id=student6.id, course_code=course6.course_code, year=semester6.year, term=semester6.term,
                              grade="A-", gpa=GRADE_TO_GPA["A-"])
    enrollment27 = Enrollment(student_id=student7.id, course_code=course6.course_code, year=semester6.year, term=semester6.term,
                              grade="B", gpa=GRADE_TO_GPA["B"])
    enrollment28 = Enrollment(student_id=student8.id, course_code=course6.course_code, year=semester6.year, term=semester6.term,
                              grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment29 = Enrollment(student_id=student9.id, course_code=course6.course_code, year=semester6.year, term=semester6.term,
                              grade="C+", gpa=GRADE_TO_GPA["C+"])
    enrollment30 = Enrollment(student_id=student10.id, course_code=course6.course_code, year=semester6.year, term=semester6.term,
                              grade="C", gpa=GRADE_TO_GPA["C"])

    # Semester 7 - Course 7
    enrollment31 = Enrollment(student_id=student1.id, course_code=course7.course_code, year=semester7.year, term=semester7.term,
                              grade="B+", gpa=GRADE_TO_GPA["B+"])
    enrollment32 = Enrollment(student_id=student2.id, course_code=course7.course_code, year=semester7.year, term=semester7.term,
                              grade="A-", gpa=GRADE_TO_GPA["A-"])
    enrollment33 = Enrollment(student_id=student3.id, course_code=course7.course_code, year=semester7.year, term=semester7.term,
                              grade="B", gpa=GRADE_TO_GPA["B"])
    enrollment34 = Enrollment(student_id=student4.id, course_code=course7.course_code, year=semester7.year, term=semester7.term,
                              grade="C", gpa=GRADE_TO_GPA["C"])
    enrollment35 = Enrollment(student_id=student5.id, course_code=course7.course_code, year=semester7.year, term=semester7.term,
                              grade="B", gpa=GRADE_TO_GPA["B"])

    # Semester 8 - Course 8
    enrollment36 = Enrollment(student_id=student6.id, course_code=course8.course_code, year=semester8.year, term=semester8.term,
                              grade="A", gpa=GRADE_TO_GPA["A"])
    enrollment37 = Enrollment(student_id=student7.id, course_code=course8.course_code, year=semester8.year, term=semester8.term,
                              grade="A-", gpa=GRADE_TO_GPA["A-"])
    enrollment38 = Enrollment(student_id=student8.id, course_code=course8.course_code, year=semester8.year, term=semester8.term,
                              grade="C+", gpa=GRADE_TO_GPA["C+"])
    enrollment39 = Enrollment(student_id=student9.id, course_code=course8.course_code, year=semester8.year, term=semester8.term,
                              grade="B-", gpa=GRADE_TO_GPA["B-"])
    enrollment40 = Enrollment(student_id=student10.id, course_code=course8.course_code, year=semester8.year, term=semester8.term,
                              grade="D", gpa=GRADE_TO_GPA["D"])

    db.session.add_all([
        enrollment1, enrollment2, enrollment3, enrollment4, enrollment5,
        enrollment6, enrollment7, enrollment8, enrollment9, enrollment10,
        enrollment11, enrollment12, enrollment13, enrollment14, enrollment15,
        enrollment16, enrollment17, enrollment18, enrollment19, enrollment20,
        enrollment21, enrollment22, enrollment23, enrollment24, enrollment25,
        enrollment26, enrollment27, enrollment28, enrollment29, enrollment30,
        enrollment31, enrollment32, enrollment33, enrollment34, enrollment35,
        enrollment36, enrollment37, enrollment38, enrollment39, enrollment40
    ])

    db.session.commit()

    print("Database seeded successfully!")
