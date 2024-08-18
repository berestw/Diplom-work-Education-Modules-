from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education_modules.models import EducationModules
from users.models import User


class EducationModulesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@mail.ru")
        self.user.set_password("1234")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.education_module = EducationModules.objects.create(
            number=1,
            name="Test Module",
            description="This is a test module",
        )

    def test_create_education_module(self):
        url = reverse("education_modules:create")
        data = {
            "number": "2",
            "name": "Test Module 2",
            "description": "This is a test module",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationModules.objects.count(), 2)
        self.assertTrue(EducationModules.objects.all().exists())

    def test_get_list_of_education_module(self):
        """
        Test retrieving a list of educational models.
        """
        self.url = reverse("education_modules:list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_education_module_retrieve(self):
        url = reverse("education_modules:retrieve", args=(self.education_module.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.education_module.name)

    def test_education_module_update(self):
        url = reverse("education_modules:update", args=(self.education_module.pk,))
        data = {
            "name": "Учебный курс",
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Учебный курс")

    def test_education_module_delete(self):
        url = reverse("education_modules:delete", args=(self.education_module.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EducationModules.objects.count(), 0)
