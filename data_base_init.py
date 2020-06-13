from mongo_proxy import ServerProxy
from constants import Collections


class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        db = ServerProxy(self.db_name)

        student_1 = db.let_me_insert([Collections.COLLECTION_STUDENT, {
            "_id": 123456,
            "first_name": "Jan",
            "last_name": "Kowalski",
            "schema_version": "1"
        }])

        employee_1 = db.let_me_insert([Collections.COLLECTION_EMPLOYEE, {
            "_id": 121212,
            "first_name": "John",
            "last_name": "Smith",
            "schema_version": "1"
        }])

        classroom_1 = db.let_me_insert([Collections.COLLECTION_CLASSROOM, {
            "_id": 1,
            "name": "B5-601",
            "description": "laboratory room",
            "schema_version": "1"
        }])

        subject_1 = db.let_me_insert([Collections.COLLECTION_SUBJECT, {
            "_id": 1,
            "name": "Rocket science",
            "employee_id": 121212,
            "schema_version": "1"
        }])

        subject_group_1 = db.let_me_insert([Collections.COLLECTION_SUBJECT_GROUP, {
            "_id": 1,
            "group_name": "Grupa 1",
            "employee_id": 121212,
            "subject_id": 123456,
            "schema_version": "1"
        }])

        classes_1 = db.let_me_insert([Collections.COLLECTION_CLASSES, {
            "_id": 1,
            "class_no": 5,
            "date_time": "2020-08-22",
            "classroom_id": 1,
            "subject_group_id": 1,
            "schema_version": "1"
        }])

        assignment_1 = db.let_me_insert([Collections.COLLECTION_ASSIGNMENT, {
            "_id": 1,
            "student_id": 123456,
            "subject_id": 1,
            "grade": 5
        }])

        student_group_1 = db.let_me_insert([Collections.COLLECTION_STUDENT_GROUP, {
            "_id": 123456,
            "subject_group_id": 1
        }])


DataBase('university')