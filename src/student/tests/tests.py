from django.test import TestCase

from student.models import Level, Student, StudentLevel


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(student_id="12345", full_name="Jane Doe")

    def test_create_student(self):
        self.assertEqual(self.student.student_id, "12345")

        self.assertEqual(self.student.full_name, "Jane Doe")

    def test_student_uuid_is_unique(self):
        student_2 = Student.objects.create(student_id="67890", full_name="John Doe")

        self.assertNotEqual(self.student.uuid, student_2.uuid)

    def test_student_string_representation(self):
        self.assertEqual(
            str(self.student), f"{self.student.full_name} ({self.student.student_id})"
        )


class LevelModelTest(TestCase):
    def setUp(self):
        self.level = Level.objects.create(level=Level.LevelTypes.FIFTH)

    def test_create_level(self):
        self.assertEqual(self.level.level, Level.LevelTypes.FIFTH)

    def test_level_choices(self):
        self.assertIn(self.level.level, dict(Level.LevelTypes.choices))

    def test_level_string_representation(self):
        self.assertEqual(str(self.level), f"{self.level.level.label} level/grade")


class StudentLevelModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(student_id="12345", full_name="John Doe")
        self.level = Level.objects.create(level=Level.LevelTypes.FIFTH)
        self.student_level = StudentLevel.objects.create(
            student=self.student,
            level=self.level,
            year=2024,
            is_current=True,
            notes="Excellent performance.",
        )

    def test_create_student_level(self):
        self.assertEqual(self.student_level.student, self.student)
        self.assertEqual(self.student_level.level, self.level)
        self.assertEqual(self.student_level.year, 2024)
        self.assertTrue(self.student_level.is_current)
        self.assertEqual(self.student_level.notes, "Excellent performance.")

    def test_student_level_uuid_is_unique(self):
        another_student_level = StudentLevel.objects.create(
            student=self.student, level=self.level, year=2023
        )
        self.assertNotEqual(self.student_level.uuid, another_student_level.uuid)

    def test_student_level_relationships(self):
        self.assertEqual(self.student.level_history.count(), 1)
        self.assertEqual(self.level.student_records.count(), 1)
