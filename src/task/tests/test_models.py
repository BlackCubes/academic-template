from django.test import TestCase

from task.models import Category, Group, Task, Type


class TypeModelTest(TestCase):
    def setUp(self):
        self.type_1 = Type.objects.create(title="Test")
        self.type_2 = Type.objects.create(title="Quiz")
        self.type_3 = Type.objects.create(title="Test/Quiz")
        self.type_4 = Type.objects.create(title="Assignment")

    def test_create_type(self):
        self.assertEqual(self.type_1.title, "Test")

        self.assertEqual(self.type_2.title, "Quiz")

        self.assertEqual(self.type_3.title, "Test/Quiz")

        self.assertEqual(self.type_4.title, "Assignment")

    def test_type_uuid_is_unique(self):
        self.assertNotEqual(self.type_1.uuid, self.type_2.uuid)
        self.assertNotEqual(self.type_1.uuid, self.type_3.uuid)
        self.assertNotEqual(self.type_1.uuid, self.type_4.uuid)

        self.assertNotEqual(self.type_2.uuid, self.type_3.uuid)
        self.assertNotEqual(self.type_2.uuid, self.type_4.uuid)

        self.assertNotEqual(self.type_3.uuid, self.type_4.uuid)

    def test_type_string_representation(self):
        self.assertEqual(str(self.type_1), f"{self.type_1.title} type")

        self.assertEqual(str(self.type_2), f"{self.type_2.title} type")

        self.assertEqual(str(self.type_3), f"{self.type_3.title} type")

        self.assertEqual(str(self.type_4), f"{self.type_4.title} type")


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(title="Assessment")
        self.category_2 = Category.objects.create(title="Assignment")

    def test_create_category(self):
        self.assertEqual(self.category_1.title, "Assessment")

        self.assertEqual(self.category_2.title, "Assignment")

    def test_category_uuid_is_unique(self):
        self.assertNotEqual(self.category_1.uuid, self.category_2.uuid)

    def test_category_string_representation(self):
        self.assertEqual(str(self.category_1), f"{self.category_1.title} category")

        self.assertEqual(str(self.category_2), f"{self.category_2.title} category")


class GroupModelTest(TestCase):
    def setUp(self):
        self.type_1 = Type.objects.create(title="Test")
        self.type_2 = Type.objects.create(title="Quiz")
        self.type_3 = Type.objects.create(title="Test/Quiz")
        self.type_4 = Type.objects.create(title="Assignment")

        self.category_1 = Category.objects.create(title="Assessment")
        self.category_2 = Category.objects.create(title="Assignment")

        self.group_1 = Group.objects.create(type=self.type_1, category=self.category_1)
        self.group_2 = Group.objects.create(type=self.type_2, category=self.category_1)
        self.group_3 = Group.objects.create(type=self.type_3, category=self.category_1)
        self.group_4 = Group.objects.create(type=self.type_4, category=self.category_2)

    def test_create_group(self):
        self.assertEqual(self.group_1.type, self.type_1)
        self.assertEqual(self.group_1.category, self.category_1)

        self.assertEqual(self.group_2.type, self.type_2)
        self.assertEqual(self.group_2.category, self.category_1)

        self.assertEqual(self.group_3.type, self.type_3)
        self.assertEqual(self.group_3.category, self.category_1)

        self.assertEqual(self.group_4.type, self.type_4)
        self.assertEqual(self.group_4.category, self.category_2)

    def test_group_uuid_is_unique(self):
        self.assertNotEqual(self.group_1.uuid, self.group_2.uuid)
        self.assertNotEqual(self.group_1.uuid, self.group_3.uuid)
        self.assertNotEqual(self.group_1.uuid, self.group_4.uuid)

        self.assertNotEqual(self.group_2.uuid, self.group_3.uuid)
        self.assertNotEqual(self.group_2.uuid, self.group_4.uuid)

        self.assertNotEqual(self.group_3.uuid, self.group_4.uuid)

    def test_group_string_representation(self):
        self.assertEqual(
            str(self.group_1), f"Group: {self.group_1.type}, {self.group_1.category}"
        )

        self.assertEqual(
            str(self.group_2), f"Group: {self.group_2.type}, {self.group_2.category}"
        )

        self.assertEqual(
            str(self.group_3), f"Group: {self.group_3.type}, {self.group_3.category}"
        )

        self.assertEqual(
            str(self.group_4), f"Group: {self.group_4.type}, {self.group_4.category}"
        )


class TaskModelTest(TestCase):
    def setUp(self):
        self.type_1 = Type.objects.create(title="Test")
        self.type_2 = Type.objects.create(title="Assignment")

        self.category_1 = Category.objects.create(title="Assessment")
        self.category_2 = Category.objects.create(title="Assignment")

        self.group_1 = Group.objects.create(type=self.type_1, category=self.category_1)
        self.group_2 = Group.objects.create(type=self.type_2, category=self.category_2)

        self.task_1 = Task.objects.create(
            group=self.group_1,
            title="Unit 2 Test",
            points=50,
            expected_at="2024-12-23T12:30:00.000Z",
        )
        self.task_2 = Task.objects.create(
            group=self.group_2,
            title="Slope Intercept Form",
            description="Use the notes taken from class to do the homework.",
            points=10,
            expected_at="2024-12-23T12:30:00.000Z",
        )

    def test_create_task(self):
        self.assertEqual(self.task_1.group, self.group_1)
        self.assertEqual(self.task_1.title, "Unit 2 Test")
        self.assertIsNone(self.task_1.description)
        self.assertEqual(self.task_1.points, 50)

        self.assertEqual(self.task_2.group, self.group_2)
        self.assertEqual(self.task_2.title, "Slope Intercept Form")
        self.assertIsNotNone(self.task_2.description)
        self.assertEqual(
            self.task_2.description,
            "Use the notes taken from class to do the homework.",
        )
        self.assertEqual(self.task_2.points, 10)

    def test_task_uuid_is_unique(self):
        self.assertNotEqual(self.task_1.uuid, self.task_2.uuid)

    def test_task_string_representation(self):
        self.assertEqual(
            str(self.task_1),
            f"'{self.task_1.title}' task: {self.task_1.points} points, {self.task_1.expected_at} expected date",
        )

        self.assertEqual(
            str(self.task_2),
            f"'{self.task_2.title}' task: {self.task_2.points} points, {self.task_2.expected_at} expected date",
        )
