from django.test import TestCase

from reports.models import MobinetReport, MoneyBack, Report


class ReportModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Report.objects.create(
            text='Текст больше 15 знаков',
            author=123144,
            author_name="author_username",
        )
        cls.task = Report.objects.get(text='Текст больше 15 знаков')

    def test_str_field(self):
        """Отображение поля __str__ объекта task"""
        task = ReportModelTest.task
        expected_object_name = task.text[:12]
        self.assertEquals(expected_object_name, str(task))


class MobinetReportModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        MobinetReport.objects.create(
            text='Текст больше 15 знаков',
            author=123144,
            author_name="author_username",
        )
        cls.task = MobinetReport.objects.get(text='Текст больше 15 знаков')

    def test_str_field(self):
        """Отображение поля __str__ объекта task"""
        task = MobinetReportModelTest.task
        expected_object_name = task.text[:12]
        self.assertEquals(expected_object_name, str(task))


class MoneyBackModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        MoneyBack.objects.create(
            text='Текст больше 15 знаков',
            author=123144,
            author_name="author_username",
            value="123.00",
            link="128542",
        )
        cls.task = MoneyBack.objects.get(text='Текст больше 15 знаков')

    def test_str_field(self):
        """Отображение поля __str__ объекта task"""
        task = MoneyBackModelTest.task
        expected_object_name = task.text[:12]
        self.assertEquals(expected_object_name, str(task))
