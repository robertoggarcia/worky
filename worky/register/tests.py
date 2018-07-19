from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from .views import Login


class TokenTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = Login.as_view()

    def test_valid_token_request(self):
        request = self.factory.post('/apps/register', {'name': 'robertogarcia', 'description': 'Test_2018'}, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_token_request(self):
        request = self.factory.post('/apps/register', {}, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

