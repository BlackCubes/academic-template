model_error_messages = {
    "student": {
        "uuid": {"unique": "The UUID is not unique"},
        "student_id": {
            "blank": "The student ID cannot be empty",
            "invalid": "Invalid value for the student ID",
            "max_length": "The student ID should not exceed 10 characters",
            "null": "The student ID cannot be empty",
            "required": "The student ID is required.",
        },
        "full_name": {
            "blank": "The full name cannot be empty",
            "invalid": "Invalid value for the full name",
            "max_length": "The full name should not exceed 10 characters",
            "null": "The full name cannot be empty",
            "required": "The full name is required.",
        },
    },
    "level": {
        "uuid": {"unique": "The UUID is not unique"},
        "level": {
            "blank": "The level cannot be empty",
            "invalid": "The level must be one of the defined choices",
            "max_value": "The level should not exceed 12",
            "min_value": "The level should not be less than 0",
            "required": "The level is required",
        },
    },
    "student_level": {
        "uuid": {"unique": "The UUID is not unique"},
        "student": {
            "blank": "The student cannot be empty",
            "does_not_exist": "The student does not exist",
            "invalid": "Invalid value for the student",
            "null": "The student cannot be empty",
            "required": "The student is required",
        },
        "level": {
            "blank": "The level cannot be empty",
            "does_not_exist": "The level does not exist",
            "invalid": "Invalid value for the level",
            "null": "The level cannot be empty",
            "required": "The level is required",
        },
        "year": {
            "blank": "The year cannot be empty",
            "invalid": "Invalid value for year",
            "max_value": "The year should not exceed the current year",
            "min_value": "The year should be between the current year and 50 years",
            "required": "The level is required",
        },
        "is_current": {
            "invalid": "Invalid value for 'is current'. Must be true or false",
            "required": "The 'is current' is required",
        },
        "notes": {
            "invalid": "Invalid value for notes",
            "max_length": "The notes must not exceed 500 characters",
        },
    },
}
