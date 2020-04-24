from django.test import TestCase, Client
from django.urls import reverse
from login.models import Student, Exam, Course, Program, InternalResult, RegularResult


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.editDetails_url = reverse('editDetails')
    def test_index_view(self):

        response = self.client.get(self.index_url)

        # user is not logged in, so system redirects to login page
        self.assertEquals(response.status_code, 302)

    def test_editDetails_view(self):

        response = self.client.get(self.editDetails_url)

        self.assertAlmostEquals(response.status_code, 302)
