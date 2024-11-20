model_error_messages = {
    "task": {
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
            "blank": "The category cannot be empty",
            "invalid": "Invalid value for the category",
            "max_length": "The category should not exceed 50 characters",
            "null": "The category cannot be empty",
            "required": "The category is required",
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
}
