from uuid import uuid4

from django.core import validators
from django.db import models

from academic.utils import current_datetime_utc
from student.models import Student
from task.models import Group, Task

from .utils import model_error_messages


class Weight(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["weight"]["uuid"],
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="weight_group",
        error_messages=model_error_messages["weight"]["group"],
    )
    weight = models.DecimalField(
        default=0.00,
        max_digits=5,
        decimal_places=2,
        error_messages=model_error_messages["weight"]["weight"],
    )


class Score(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["score"]["uuid"],
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="score_task",
        error_messages=model_error_messages["score"]["task"],
    )
    score = models.PositiveIntegerField(
        default=0,
        validators=[
            validators.MinValueValidator(limit_value=0),
        ],
        error_messages=model_error_messages["score"]["score"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class ScoreStudent(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["score_student"]["uuid"],
    )
    score = models.ForeignKey(
        Score,
        on_delete=models.CASCADE,
        related_name="student_scores",
        error_messages=model_error_messages["score_student"]["score"],
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="score_history",
        error_messages=model_error_messages["score_student"]["student"],
    )
    submitted_at = models.DateTimeField(
        default=current_datetime_utc(),
        error_messages=model_error_messages["score_student"]["submitted_at"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
