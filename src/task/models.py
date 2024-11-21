from uuid import uuid4

from django.core import validators
from django.db import models

from academic.utils import current_datetime_utc

from .utils import model_error_messages


class Type(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["type"]["uuid"],
    )
    title = models.CharField(
        max_length=50, error_messages=model_error_messages["type"]["title"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} type"


class Category(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["category"]["uuid"],
    )
    title = models.CharField(
        max_length=50, error_messages=model_error_messages["category"]["title"]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} category"


class Group(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["group"]["uuid"],
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="group_type",
        error_messages=model_error_messages["group"]["type"],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="group_category",
        error_messages=model_error_messages["group"]["category"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Group: {self.type}, {self.category}"


class Task(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        error_messages=model_error_messages["task"]["uuid"],
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="task_group",
        error_messages=model_error_messages["task"]["group"],
    )
    title = models.CharField(
        max_length=100, error_messages=model_error_messages["task"]["title"]
    )
    description = models.TextField(
        null=True,
        blank=True,
        max_length=500,
        error_messages=model_error_messages["task"]["description"],
    )
    points = models.PositiveIntegerField(
        default=0,
        validators=[
            validators.MinValueValidator(limit_value=0),
        ],
        error_messages=model_error_messages["task"]["points"],
    )
    expected_at = models.DateTimeField(
        default=current_datetime_utc(),
        error_messages=model_error_messages["task"]["expected_at"],
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"'{self.title}' task: {self.points} points, {self.expected_at} expected date"
