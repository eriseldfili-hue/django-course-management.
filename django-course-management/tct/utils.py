from rest_framework.exceptions import ValidationError
from django.db import transaction

from tct.student.models import Student


@transaction.atomic
def enroll_student(course, student_ids):
    """
    Enroll multiple students into a course
    """

    # get students that exist in database
    students_to_enroll = Student.objects.filter(id__in=student_ids)

    # get already enrolled student ids
    enrolled_ids = course.student.values_list("id", flat=True)

    # remove students that are already enrolled
    students_to_add = students_to_enroll.exclude(id__in=enrolled_ids)

    if not students_to_add.exists():
        raise ValidationError(
            "All provided students are already enrolled!"
        )

    # add new students
    course.student.add(*students_to_add)

    # update number_of_students field
    course.number_of_students = course.student.count()
    course.save(update_fields=["number_of_students"])

    # return newly enrolled students
    return list(students_to_add.values_list("id", flat=True))


@transaction.atomic
def unenroll_student(course, student_ids):
    """
    Remove students from a course
    """

    # students requested for removal
    students_to_unenroll = Student.objects.filter(id__in=student_ids)

    # students currently enrolled
    enrolled_ids = course.student.values_list("id", flat=True)

    # only remove those actually enrolled
    students_to_remove = students_to_unenroll.filter(id__in=enrolled_ids)

    if not students_to_remove.exists():
        raise ValidationError(
            "None of these students are enrolled!"
        )

    # remove students
    course.student.remove(*students_to_remove)

    # update count
    course.number_of_students = course.student.count()
    course.save(update_fields=["number_of_students"])

    # return removed students
    return list(students_to_remove.values_list("id", flat=True))