from mongo_proxy import ServerProxy
from constants import Collections as Cls


def catch_exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            print('Duplicated document in: ', func.__name__)
            return None
    return wrapper


class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = ServerProxy(self.db_name)

    @catch_exception_decorator
    def init_student(self, id, f_name, n_name, l_name):
        student_2 = self.db.let_me_insert([Cls.COLLECTION_STUDENT, {
            "_id": id,
            "first_name": [
                {
                    "full_name": f_name
                },
                {
                    "nick_name": n_name
                }
            ],
            "last_name": l_name,
            "schema_version": Cls.SCHEMA_VERSION
        }])

    @catch_exception_decorator
    def init_employee(self, id, f_name, l_name):
        employee_1 = self.db.let_me_insert([Cls.COLLECTION_EMPLOYEE, {
            "_id": id,
            "first_name": f_name,
            "last_name": l_name,
            "schema_version": Cls.SCHEMA_VERSION
        }])

    @catch_exception_decorator
    def init_clasroom(self):
        classroom_1 = self.db.let_me_insert([Cls.COLLECTION_CLASSROOM, {
            "_id": 1,
            "name": "B5-601",
            "description": "laboratory room",
            "schedule": [
                {
                    "date_time": "2020-08-20"
                },
                {
                    "employee_id": 121212
                },
                {
                    "subject_name": "Rocket science"
                },
            ],
            "schema_version": Cls.SCHEMA_VERSION
        }])

    @catch_exception_decorator
    def init_subject(self, id, employee_id, lang, exam):
        subject_1 = self.db.let_me_insert([Cls.COLLECTION_SUBJECT, {
            "_id": id,
            "name": "Rocket science",
            "subject_details": [
                {
                    "employee_id": employee_id
                },
                {
                    "lecture_language": lang
                },
                {
                    "examination": exam
                }

            ],
            "schema_version": Cls.SCHEMA_VERSION
        }])

    def subject_minor_info(self, subject_id, ects, description, hours):
        subj_minor_1 = self.db.let_me_insert([Cls.COLLECTION_SUBJECT_MINOR, {
            "subject_id": subject_id,
            "ects": ects,
            "description": description,
            "hours_number": hours
        }])

    @catch_exception_decorator
    def init_subject_group(self):
        subject_group_1 = self.db.let_me_insert([Cls.COLLECTION_SUBJECT_GROUP, {
            "_id": 1,
            "group_name": "Grupa 1",
            "employee_id": 121212,
            "subject_id": 123456,
            "schema_version": Cls.SCHEMA_VERSION
        }])

    @catch_exception_decorator
    def init_classes(self):
        classes_1 = self.db.let_me_insert([Cls.COLLECTION_CLASSES, {
            "_id": 1,
            "class_no": 5,
            "date_time": "2020-08-22",
            "classroom_id": 1,
            "subject_group_id": 1,
            "schema_version": Cls.SCHEMA_VERSION
        }])

    @catch_exception_decorator
    def init_assignment(self):
        assignment_1 = self.db.let_me_insert([Cls.COLLECTION_ASSIGNMENT, {
            "_id": 1,
            "student_id": 123456,
            "subject_id": 1,
            "grade": 5,
            "schema_version": Cls.SCHEMA_VERSION
        }])

    @catch_exception_decorator
    def init_student_group(self):
        student_group_1 = self.db.let_me_insert([Cls.COLLECTION_STUDENT_GROUP, {
            "_id": 123456,
            "subject_group_id": 1,
            "schema_version": Cls.SCHEMA_VERSION
        }])

    def init_field_of_study(self):
        field_1 = self.db.let_me_insert([Cls.COLLECTION_FIELD_OF_STUDY, {
            "_id": 1,
            "name": "Informatyka techniczna",
            "disciplines": [
                "Informatyka techniczna i telekomunikacja",
                "Inzynieria materialowa"
            ],
            "schema_version": Cls.SCHEMA_VERSION
        }])


db = DataBase('university')
db.init_field_of_study()