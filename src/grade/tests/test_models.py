from django.test import TestCase

from grade.models import Score, ScoreStudent, Weight
from student.models import Student
from task.models import Category, Group, Task, Type


class WeightModelTest(TestCase):
    def setUp(self):
        self.test_type = Type.objects.create(title="Test")
        self.quiz_type = Type.objects.create(title="Quiz")
        self.assignment_type = Type.objects.create(title="Assignment")

        self.assessment_category = Category.objects.create(title="Assessment")
        self.assignment_category = Category.objects.create(title="Assignment")

        self.test_group = Group.objects.create(
            type=self.test_type, category=self.assessment_category
        )
        self.quiz_group = Group.objects.create(
            type=self.quiz_type, category=self.assessment_category
        )
        self.assignment_group = Group.objects.create(
            type=self.assignment_type, category=self.assignment_category
        )

        self.test_weight = Weight.objects.create(group=self.test_group, weight=0.60)
        self.quiz_weight = Weight.objects.create(group=self.quiz_group, weight=0.30)
        self.assignment_weight = Weight.objects.create(
            group=self.assignment_group, weight=0.10
        )

    def test_create_weight(self):
        self.assertEqual(self.test_weight.group, self.test_group)
        self.assertEqual(self.test_weight.weight, 0.60)

        self.assertEqual(self.quiz_weight.group, self.quiz_group)
        self.assertEqual(self.quiz_weight.weight, 0.30)

        self.assertEqual(self.assignment_weight.group, self.assignment_group)
        self.assertEqual(self.assignment_weight.weight, 0.10)

    def test_weight_uuid_is_unique(self):
        self.assertNotEqual(self.test_weight.uuid, self.quiz_weight.uuid)
        self.assertNotEqual(self.test_weight.uuid, self.assignment_weight.uuid)
        self.assertNotEqual(self.assignment_weight.uuid, self.quiz_weight.uuid)

    def test_weight_string_representation(self):
        self.assertEqual(
            str(self.test_weight),
            f"{self.test_weight.weight} weight for {self.test_weight.group}",
        )

        self.assertEqual(
            str(self.quiz_weight),
            f"{self.quiz_weight.weight} weight for {self.quiz_weight.group}",
        )

        self.assertEqual(
            str(self.assignment_weight),
            f"{self.assignment_weight.weight} weight for {self.assignment_weight.group}",
        )


class ScoreModelTest(TestCase):
    def setUp(self):
        self.test_type = Type.objects.create(title="Test")
        self.quiz_type = Type.objects.create(title="Quiz")
        self.assignment_type = Type.objects.create(title="Assignment")

        self.assessment_category = Category.objects.create(title="Assessment")
        self.assignment_category = Category.objects.create(title="Assignment")

        self.test_group = Group.objects.create(
            type=self.test_type, category=self.assessment_category
        )
        self.quiz_group = Group.objects.create(
            type=self.quiz_type, category=self.assessment_category
        )
        self.assignment_group = Group.objects.create(
            type=self.assignment_type, category=self.assignment_category
        )

        self.test_task = Task.objects.create(
            group=self.test_group,
            title="Unit 2 Test",
            points=50,
            expected_at="2024-12-23T12:30:00.000Z",
        )
        self.quiz_task = Task.objects.create(
            group=self.quiz_group,
            title="Unit 2B Quiz",
            points=25,
            expected_at="2024-12-23T12:30:00.000Z",
        )
        self.assignment_task = Task.objects.create(
            group=self.assignment_group,
            title="Slope Intercept Form",
            description="Use the notes taken from class to do the homework.",
            points=10,
            expected_at="2024-12-23T12:30:00.000Z",
        )

        self.test_score = Score.objects.create(task=self.test_task, score=40)
        self.quiz_score = Score.objects.create(task=self.quiz_task, score=23)
        self.assignment_score = Score.objects.create(task=self.assignment_task, score=4)

    def test_create_score(self):
        self.assertEqual(self.test_score.task, self.test_task)
        self.assertEqual(self.test_score.score, 40)

        self.assertEqual(self.quiz_score.task, self.quiz_task)
        self.assertEqual(self.quiz_score.score, 23)

        self.assertEqual(self.assignment_score.task, self.assignment_task)
        self.assertEqual(self.assignment_score.score, 4)

    def test_score_uuid_is_unique(self):
        self.assertNotEqual(self.test_score.uuid, self.quiz_score.uuid)
        self.assertNotEqual(self.test_score.uuid, self.assignment_score.uuid)
        self.assertNotEqual(self.assignment_score.uuid, self.quiz_score.uuid)

    def test_score_string_representation(self):
        self.assertEqual(
            str(self.test_score),
            f"{self.test_score.score} score for {self.test_score.task}",
        )

        self.assertEqual(
            str(self.quiz_score),
            f"{self.quiz_score.score} score for {self.quiz_score.task}",
        )

        self.assertEqual(
            str(self.assignment_score),
            f"{self.assignment_score.score} score for {self.assignment_score.task}",
        )


class ScoreStudentModelTest(TestCase):
    def setUp(self):
        self.test_type = Type.objects.create(title="Test")
        self.quiz_type = Type.objects.create(title="Quiz")
        self.assignment_type = Type.objects.create(title="Assignment")

        self.assessment_category = Category.objects.create(title="Assessment")
        self.assignment_category = Category.objects.create(title="Assignment")

        self.test_group = Group.objects.create(
            type=self.test_type, category=self.assessment_category
        )
        self.quiz_group = Group.objects.create(
            type=self.quiz_type, category=self.assessment_category
        )
        self.assignment_group = Group.objects.create(
            type=self.assignment_type, category=self.assignment_category
        )

        self.test_task = Task.objects.create(
            group=self.test_group,
            title="Unit 2 Test",
            points=50,
            expected_at="2024-12-23T12:30:00.000Z",
        )
        self.quiz_task = Task.objects.create(
            group=self.quiz_group,
            title="Unit 2B Quiz",
            points=25,
            expected_at="2024-12-23T12:30:00.000Z",
        )
        self.assignment_task = Task.objects.create(
            group=self.assignment_group,
            title="Slope Intercept Form",
            description="Use the notes taken from class to do the homework.",
            points=10,
            expected_at="2024-12-23T12:30:00.000Z",
        )

        self.test_score = Score.objects.create(task=self.test_task, score=40)
        self.quiz_score = Score.objects.create(task=self.quiz_task, score=23)
        self.assignment_score = Score.objects.create(task=self.assignment_task, score=4)

        self.student = Student.objects.create(student_id="12345", full_name="Jane Doe")

        self.test_score_student = ScoreStudent.objects.create(
            score=self.test_score,
            student=self.student,
            submitted_at="2024-12-20T10:00:00.000Z",
        )
        self.quiz_score_student = ScoreStudent.objects.create(
            score=self.quiz_score,
            student=self.student,
            submitted_at="2024-12-20T10:00:00.000Z",
        )
        self.assignment_score_student = ScoreStudent.objects.create(
            score=self.assignment_score,
            student=self.student,
            submitted_at="2024-12-20T10:00:00.000Z",
        )

    def test_create_score_student(self):
        self.assertEqual(self.test_score_student.score, self.test_score)
        self.assertEqual(self.test_score_student.student, self.student)

        self.assertEqual(self.quiz_score_student.score, self.quiz_score)
        self.assertEqual(self.quiz_score_student.student, self.student)

        self.assertEqual(self.assignment_score_student.score, self.assignment_score)
        self.assertEqual(self.assignment_score_student.student, self.student)

    def test_score_student_uuid_is_unique(self):
        self.assertNotEqual(self.test_score_student.uuid, self.quiz_score_student.uuid)
        self.assertNotEqual(
            self.test_score_student.uuid, self.assignment_score_student.uuid
        )
        self.assertNotEqual(
            self.assignment_score_student.uuid, self.quiz_score_student.uuid
        )

    def test_score_student_string_representation(self):
        self.assertEqual(
            str(self.test_score_student),
            f"{self.test_score_student.student} student submitted at {self.test_score_student.submitted_at} with a {self.test_score_student.score}",
        )

        self.assertEqual(
            str(self.quiz_score_student),
            f"{self.quiz_score_student.student} student submitted at {self.quiz_score_student.submitted_at} with a {self.quiz_score_student.score}",
        )

        self.assertEqual(
            str(self.assignment_score_student),
            f"{self.assignment_score_student.student} student submitted at {self.assignment_score_student.submitted_at} with a {self.assignment_score_student.score}",
        )
