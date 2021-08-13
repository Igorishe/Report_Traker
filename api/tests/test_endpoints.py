from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from reports.models import Report


class APITests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user = User.objects.create(username='test_admin')
        user.set_password('some_pass')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        cls.user = user
        cls.report_new = Report.objects.create(
            author=123456,
            text='Test_text',
            status='New'
        )
        cls.report_closed = Report.objects.create(
            author=123456,
            text='Test_text2',
            status='Closed'
        )

    def setUp(self):
        self.admin_client = APIClient()
        self.admin_client.force_login(APITests.user)

    def test_admin_create_token(self):
        """
        Ensure admin can create a new token.
        """
        url = reverse('authorization')
        data = {
            'username': 'test_admin',
            'password': 'some_pass',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, 'Status code is not 200'
        )
        self.assertEqual(
            Token.objects.count(), 1, 'Token has not been created'
        )
        self.assertEqual(
            Token.objects.get().user,
            APITests.user,
            'Token has been attached for wrong user'
        )

    def test_reports_listing(self):
        """
        Ensure GET-request receives right listing
        """
        url = reverse('reports')
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, 'Status code is not 200'
        )
        self.assertEqual(
            response.data[0].get('text'),
            APITests.report_new.text,
            'Listing responds wrong objects'
        )

    def test_reports_create(self):
        """
        Ensure POST-request creates reports objects
        """
        url = reverse('reports')
        data = [
            {
                'author': 123123,
                'text': 'Test report3'
            },
            {
                'author': 123123,
                'text': 'Test report4'
            }
        ]
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, 'Status is not 201'
        )
        self.assertEqual(
            Report.objects.count(), 4, 'Post objects have not created'
        )
        self.assertEqual(
            response.data[0].get('text'),
            data[0].get('text')
        )
