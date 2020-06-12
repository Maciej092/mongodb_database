from marshmallow import Schema, fields


class StudentSchema(Schema):
    student_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    created_at = fields.DateTime()


class EmployeeSchema(Schema):
    employee_id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    created_at = fields.DateTime()


class AssignmentSchema(Schema):
    assignment_id = fields.Int()
    student_id = fields.Dict()
    subject_id = fields.Dict()
    grade = fields.Float()


class ClassroomSchema(Schema):
    classroom_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()


class ClassesSchema(Schema):
    classes_id = fields.Int()
    class_no = fields.Int()
    date_time = fields.DateTime()
    classroom_id = fields.Int()
    group_subject_id = fields.Int()


class StudentGroupSchema(Schema):
    student_id = fields.Dict()
    group_subject_id = fields.Int()


class SubjectGroupSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
