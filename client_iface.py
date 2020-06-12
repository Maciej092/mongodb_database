from mongo_proxy import MyMongo
from constants import Collections


def add_student():
    first_name = input("Podaj swoje imie")
    last_name = input("Podaj swoje nazwisko")
    student_id = input("Podaj swoj numer id")

    data = {
        "student_id": student_id,
        "first_name": first_name,
        "last_name": last_name,
        "schema_version": "1"
    }
    return Collections.COLLECTION_STUDENT, data


def add_employee():
    first_name = input("Podaj swoje imie")
    last_name = input("Podaj swoje nazwisko")
    employee_id = input("Podaj swoj numer id")

    data = {
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "schema_version": "1"
    }
    return Collections.COLLECTION_EMPLOYEE, data


db = MyMongo('university')
db.let_me_insert(add_student())
db.let_me_insert(add_employee())


