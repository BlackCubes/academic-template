model_error_messages = {
    "type": {
        "uuid": {"unique": "The UUID is not unique"},
        "title": {
            "blank": "The title cannot be empty",
            "invalid": "Invalid value for the title",
            "max_length": "The title should not exceed 50 characters",
            "null": "The title cannot be empty",
            "required": "The title is required",
        },
    },
    "category": {
        "uuid": {"unique": "The UUID is not unique"},
        "title": {
            "blank": "The title cannot be empty",
            "invalid": "Invalid value for the title",
            "max_length": "The title should not exceed 50 characters",
            "null": "The title cannot be empty",
            "required": "The title is required",
        },
    },
    "group": {
        "uuid": {"unique": "The UUID is not unique"},
        "type": {
            "blank": "The type cannot be empty",
            "does_not_exist": "The type does not exist",
            "invalid": "Invalid value for the type",
            "null": "The type cannot be empty",
            "required": "The type is required",
        },
        "category": {
            "blank": "The category cannot be empty",
            "does_not_exist": "The category does not exist",
            "invalid": "Invalid value for the category",
            "null": "The category cannot be empty",
            "required": "The category is required",
        },
    },
    "task": {
        "uuid": {"unique": "The UUID is not unique"},
        "group": {
            "blank": "The group cannot be empty",
            "does_not_exist": "The group does not exist",
            "invalid": "Invalid value for the group",
            "null": "The group cannot be empty",
            "required": "The group is required",
        },
        "title": {
            "blank": "The title cannot be empty",
            "invalid": "Invalid value for the title",
            "max_length": "The title should not exceed 100 characters",
            "null": "The title cannot be empty",
            "required": "The title is required",
        },
        "description": {
            "invalid": "Invalid value for description",
            "max_length": "The description must not exceed 500 characters",
        },
        "points": {
            "blank": "The points cannot be empty",
            "invalid": "Invalid value for points",
            "min_value": "The points should be more than 0",
            "required": "The points is required",
        },
        "expected_at": {
            "blank": "The expected date cannot be empty",
            "invalid": "Invalid UTC datetime value for the expected date",
            "invalid_date": "Invalid date value for the expected date",
            "invalid_datetime": "Invalid UTC datetime value for the expected date",
            "null": "The expected date cannot be empty",
            "required": "The expected date is required",
        },
    },
}
