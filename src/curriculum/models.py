from uuid import uuid4

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.utils import current_datetime_utc
from student.models import Student

from .utils import model_error_messages

# from task.models import Task


class Teacher(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["teacher"]["uuid"],
    )
    teacher_id = models.CharField(
        max_length=10, error_messages=model_error_messages["teacher"]["teacher_id"]
    )
    full_name = models.CharField(
        max_length=100, error_messages=model_error_messages["teacher"]["full_name"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.teacher_id})"


class Room(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["room"]["uuid"],
    )
    room_number = models.CharField(
        max_length=10, error_messages=model_error_messages["room"]["room_number"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.room_number} room"


class Subject(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["subject"]["uuid"],
    )
    title = models.CharField(
        max_length=100, error_messages=model_error_messages["subject"]["title"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"'{self.title}' subject"


class Period(models.Model):
    class PeriodTypes(models.IntegerChoices):
        PERIOD_ZERO = 0, _("Period 0")
        PERIOD_ONE = 1, _("Period 1")
        PERIOD_TWO = 2, _("Period 2")
        PERIOD_THREE = 3, _("Period 3")
        PERIOD_FOUR = 4, _("Period 4")
        PERIOD_FIVE = 5, _("Period 5")
        PERIOD_SIX = 6, _("Period 6")
        PERIOD_SEVEN = 7, _("Period 7")
        PERIOD_EIGHT = 8, _("Period 8")

    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        # error_messages=
    )
    period = models.PositiveIntegerField(
        choices=PeriodTypes,
        default=PeriodTypes.PERIOD_ONE,
        validators=[
            validators.MinValueValidator(limit_value=0),
            validators.MaxValueValidator(limit_value=PeriodTypes.__len__),
        ],
        # error_messages=
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.period.label}"


# TITLE MUST BE UNIQUE!!!
class Curriculum(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        # error_messages=model_error_messages["course"]["uuid"],
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="course_subject",
        # error_messages=
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="course_room",
        # error_messages=
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        related_name="course_period",
        # error_messages=
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="course_teacher",
        # error_messages=
    )
    title = models.CharField(
        max_length=100,
        # error_messages=
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=500,
        # error_messages=model_error_messages["task"]["description"],
    )
    started_at = models.DateTimeField(
        default=current_datetime_utc(),
        # error_messages=
    )
    end_at = models.DateTimeField(
        null=True,
        blank=True,
        # error_messages=
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


# TODO: CurriculumTeacher and CurriculumStudent
class CurriculumStudent(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        # error_messages=model_error_messages["course"]["uuid"],
    )
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="task_curricula",
        # error_messages=
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="curriculum_students",
        # error_messages=
    )
    is_current = models.BooleanField(
        default=False,
        # error_messages=
    )
    started_at = models.DateTimeField(
        default=current_datetime_utc(),
        # error_messages=
    )
    end_at = models.DateTimeField(
        null=True,
        blank=True,
        # error_messages=
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
