class DataBase:
    host_name = 'localhost'
    port = 27017


class Collections:
    SCHEMA_VERSION = "1"

    COLLECTION_STUDENT = 'student'
    COLLECTION_EMPLOYEE = 'employee'
    COLLECTION_ASSIGNMENT = 'assignment'
    COLLECTION_CLASSROOM = 'classroom'
    COLLECTION_CLASSES = 'classes'
    COLLECTION_SUBJECT = 'subject'
    COLLECTION_STUDENT_GROUP = 'student_group'
    COLLECTION_SUBJECT_GROUP = 'subject_group'
    COLLECTION_SUBJECT_MINOR = 'subject_minor_info'
    COLLECTION_FIELD_OF_STUDY = 'field_of_study'
