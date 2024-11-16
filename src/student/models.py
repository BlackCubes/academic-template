from uuid import uuid4

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.utils import current_year

from .utils import model_error_messages


class Student(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["student"]["uuid"],
    )
    student_id = models.CharField(
        max_length=10, error_messages=model_error_messages["student"]["student_id"]
    )
    full_name = models.CharField(
        max_length=100, error_messages=model_error_messages["student"]["full_name"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.full_name} ({self.student_id})"


class Level(models.Model):
    class LevelTypes(models.IntegerChoices):
        KINDERGARTEN = 0, _("Kindergarten")
        FIRST = 1, _("1st")
        SECOND = 2, _("2nd")
        THIRD = 3, _("3rd")
        FOURTH = 4, _("4th")
        FIFTH = 5, _("5th")
        SIXTH = 6, _("6th")
        SEVENTH = 7, _("7th")
        EIGHTH = 8, _("8th")
        NINTH = 9, _("9th")
        TENTH = 10, _("10th")
        ELEVENTH = 11, _("11th")
        TWELFTH = 12, _("12th")

    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["level"]["uuid"],
    )
    level = models.PositiveIntegerField(
        choices=LevelTypes,
        default=LevelTypes.KINDERGARTEN,
        validators=[
            validators.MinValueValidator(limit_value=0),
            validators.MaxValueValidator(limit_value=12),
        ],
        error_messages=model_error_messages["level"]["level"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.level.label} level/grade"


class StudentLevel(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["student_level"]["uuid"],
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="level_history",
        error_messages=model_error_messages["student_level"]["student"],
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name="student_records",
        error_messages=model_error_messages["student_level"]["level"],
    )
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[
            validators.MinValueValidator(limit_value=(current_year() - 50)),
            validators.MaxValueValidator(limit_value=(current_year())),
        ],
        error_messages=model_error_messages["student_level"]["year"],
    )
    is_current = models.BooleanField(
        default=False,
        error_messages=model_error_messages["student_level"]["is_current"],
    )
    notes = models.TextField(
        null=True,
        blank=True,
        max_length=500,
        error_messages=model_error_messages["student_level"]["notes"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.student}, {self.level}, {self.year}, {'current' if self.is_current else 'not current'}"
