# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
# from users.models import User
# from .models import EducationModules
#
#
# class EducationModulesAPITestCase(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(email='test@mail.ru', password='test', is_staff=True,
#                                         is_superuser=True)
#         self.client.force_authenticate(user=self.user)
#         self.model_data = {
#             'number': 1,
#             'name': 'Test Module',
#             'description': 'Test Module',
#         }
#         self.create_url = '/models/create/'
#         self.update_url = '/models/update/'
#         self.delete_url = '/models/delete/'
#
#     def test_create_module(self):
#         response = self.client.post(self.create_url, self.model_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(EducationModules.objects.count(), 1)
#         self.assertEqual(EducationModules.objects.get().name, self.model_data['name'])
#
#     def test_get_list_of_modules(self):
#         EducationModules.objects.create(**self.model_data)
#         response = self.client.get('/models/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data['results']), 1)
#
#     def test_update_module(self):
#         model = EducationModules.objects.create(**self.model_data)
#         updated_data = {
#             'number': 2,
#             'name': 'Обновленный модуль',
#             'description': 'Здесь измененный модуль',
#         }
#         response = self.client.put(f'{self.update_url}{model.id}/', updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         model.refresh_from_db()
#         self.assertEqual(model.name, updated_data['name'])
#
#     def test_delete_module(self):
#         model = EducationModules.objects.create(**self.model_data)
#         response = self.client.delete(f'{self.delete_url}{model.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(EducationModules.objects.filter(id=model.id).exists())

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
