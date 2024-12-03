model_error_messages = {
    "weight": {
        "uuid": {"unique": "The UUID is not unique"},
        "group": {
            "blank": "The group cannot be empty",
            "does_not_exist": "The group does not exist",
            "invalid": "Invalid value for the group",
            "null": "The group cannot be empty",
            "required": "The group is required",
        },
        "weight": {
            "blank": "The weight cannot be empty",
            "invalid": "Invalid decimal value for the weight",
            "min_value": "The weight should be more than 0.00",
            "max_value": "The weight should be less than 100.00",
            "max_digits": "The weight should be less than 5 digits",
            "required": "The full name is required.",
        },
    },
    "score": {
        "uuid": {"unique": "The UUID is not unique"},
        "task": {
            "blank": "The task cannot be empty",
            "does_not_exist": "The task does not exist",
            "invalid": "Invalid value for the task",
            "null": "The task cannot be empty",
            "required": "The task is required",
        },
        "score": {
            "blank": "The score cannot be empty",
            "invalid": "Invalid value for score",
            "min_value": "The score should be more than 0",
            "required": "The score is required",
        },
    },
    "score_student": {
        "uuid": {"unique": "The UUID is not unique"},
        "score": {
            "blank": "The score cannot be empty",
            "does_not_exist": "The score does not exist",
            "invalid": "Invalid value for the score",
            "null": "The score cannot be empty",
            "required": "The score is required",
        },
        "student": {
            "blank": "The student cannot be empty",
            "does_not_exist": "The student does not exist",
            "invalid": "Invalid value for the student",
            "null": "The student cannot be empty",
            "required": "The student is required",
        },
        "submitted_at": {
            "blank": "The submitted date cannot be empty",
            "invalid": "Invalid UTC datetime value for the submitted date",
            "invalid_date": "Invalid date value for the submitted date",
            "invalid_datetime": "Invalid UTC datetime value for the submitted date",
            "null": "The submitted date cannot be empty",
            "required": "The submitted date is required",
        },
    },
}
