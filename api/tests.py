from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import  get_user_model
from .models import Expense
from django.shortcuts import reverse

# Create your tests here.
class ApiTesting(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.testuser1 =get_user_model().objects.create_user(username="testuser1",password="test123")
        cls.testuser2 = get_user_model().objects.create_user(username="testuser2", password="test123")
        cls.testuser3 = get_user_model().objects.create_user(username="testuser3", password="test123")

    def test_add_expenses_percentage_method(self):
        data = {
            "name": "hangout",
            "total_bill": 4299,
            "billing_method": "PE",
            "owned_by": [
                {"username": "testuser1", "owes": "50%"},
                {"username": "testuser2", "owes": "25%"},
                {"username": "testuser3", "owes": "25%"}

            ]
        }
        self.client.login(username="testuser1",password="test123")
        response = self.client.post(reverse("api:add-expenses"),data,format="json")
        self.assertEqual(response.status_code,201)

    def test_add_expenses_equal_method(self):
        data = {
            "name": "hangout",
            "total_bill": 3000,
            "billing_method": "EQ",
            "owned_by": [
                {"username": "testuser1", "owes": "1000"},
                {"username": "testuser2", "owes": "1000"},
                {"username": "testuser3", "owes": "1000"}

            ]
        }
        self.client.login(username="testuser1", password="test123")
        response = self.client.post(reverse("api:add-expenses"), data, format="json")
        self.assertEqual(response.status_code, 201)
    def test_add_expenses_exact_method(self):
        data = {
            "name": "hangout",
            "total_bill": 3000,
            "billing_method": "EX",
            "owned_by": [
                {"username": "testuser1", "owes": "1000"},
                {"username": "testuser2", "owes": "1000"},
                {"username": "testuser3", "owes": "1000"}

            ]
        }
        self.client.login(username="testuser1", password="test123")
        response = self.client.post(reverse("api:add-expenses"), data, format="json")
        self.assertEqual(response.status_code, 201)
