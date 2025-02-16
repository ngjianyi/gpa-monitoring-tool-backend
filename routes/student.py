from flask import Blueprint, jsonify, request

from models.models import db, Student, Teacher

bp = Blueprint('students', __name__)

@bp.route('/students', methods=['GET'])
def get_students():
    """
    Get a list of all students, their assigned teacher's name, and cumulative GPA.

    Request:
        - Method: GET
        - No query parameters

    Response:
        - Status Code: 200 OK
        - Body: List of students with their teacher's name and cumulative GPA
    """

    students = Student.query.all()
    response = []
    for student in students:
        total_gpa = 0
        total_courses = 0

        for enrollment in student.enrollments:
            total_gpa += enrollment.gpa
            total_courses += 1

        cumulative_gpa = round(total_gpa / total_courses, 2) if total_courses > 0 else None
        teacher_name = student.teacher.name if student.teacher else 'No teacher assigned'

        response.append({
            "student_name": student.name,
            "teacher_name": teacher_name,
            "cumulative_gpa": cumulative_gpa
        })

    return jsonify(response), 200


@bp.route('/students/reassign', methods=['POST'])
def reassign_student():
    """
    Reassign a student to a new teacher.

    Request:
        - Method: POST
        - Body: JSON with 'student_id' and 'teacher_id'
        - Example Request Body:

    Response:
        - Status Code: 200 OK if reassigned successfully
        - Status Code: 400 Bad Request if missing required fields
        - Status Code: 404 Not Found if student or teacher is not found
    """

    data = request.get_json()

    if 'student_id' not in data or 'teacher_id' not in data:
        return jsonify({"error": "Missing required fields: 'student_id' and 'teacher_id'"}), 400

    student = Student.query.get(data['student_id'])
    new_teacher = Teacher.query.get(data['teacher_id'])

    if not student or not new_teacher:
        return jsonify({"error": "Student or Teacher not found"}), 404

    student.teacher_id = new_teacher.id
    db.session.commit()
    
    return jsonify({"message": "Student reassigned successfully."}), 200


@bp.route('/students/gpa', methods=['GET'])
def get_students_gpa_in_timeframe():
    """
    Get students' GPAs within a given timeframe (inclusive).

    Request:
        - Method: GET
        - Query Parameters:
            - start_year (required): Start year of the timeframe
            - end_year (required): End year of the timeframe
            - start_term (required): Start term of the timeframe (1 or 2)
            - end_term (required): End term of the timeframe (1 or 2)

    Response:
        - Status Code: 200 OK
        - Body: List of students with their teacher's name and cumulative GPA within the specified timeframe
    """

    start_year = request.args.get('start_year', type=int)
    end_year = request.args.get('end_year', type=int)
    start_term = request.args.get('start_term', type=int)
    end_term = request.args.get('end_term', type=int)

    if None in [start_year, end_year, start_term, end_term]:
        return jsonify({"error": "Missing required query parameters."}), 400
    
    if start_year > end_year or (start_year == end_year and start_term > end_term):
        return jsonify({"error": "Invalid timeframe, start year/term must not be greater than end year/term."}), 400

    students = Student.query.all()
    student_data = []

    for student in students:
        cumulative_gpa = 0
        total_courses = 0

        for enrollment in student.enrollments:
            if ((enrollment.year > start_year or (enrollment.year == start_year and enrollment.term >= start_term)) and
                (enrollment.year < end_year or (enrollment.year == end_year and enrollment.term <= end_term))):
                cumulative_gpa += enrollment.gpa
                total_courses += 1

        cumulative_gpa = round(cumulative_gpa / total_courses, 2) if total_courses > 0 else None
        teacher_name = student.teacher.name if student.teacher else 'No teacher assigned'

        student_data.append({
            'student_name': student.name,
            'teacher_name': teacher_name,
            'cumulative_gpa_in_timeframe': cumulative_gpa
        })

    return jsonify(student_data), 200
