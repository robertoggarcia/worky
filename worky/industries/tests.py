from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from .views import list_category
from register.views import Login


class CategoryTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = list_category

        login_view = Login.as_view()
        request = self.factory.post('/apps/register', {'name': 'robertogarcia', 'description': 'Test_2018'}, format='json')
        response = login_view(request)
        self.token = response.data['token']

    def test_not_token_industries_request(self):
        request = self.factory.get('/industries')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_industries_request(self):
        request = self.factory.get('/industries', HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)