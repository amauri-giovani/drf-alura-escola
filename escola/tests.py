from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from escola.models import Curso
import base64


class CursoViewSetTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='admin', password='123')
        self.client = APIClient()
        credentials = base64.b64encode(b'admin:123').decode('utf-8')
        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {credentials}')
        Curso.objects.create(
            codigo='PY001',
            descricao='Python',
            nivel='B'
        )

    def test_retorna_descricao_python(self):
        response = self.client.get('/cursos/', format='json')
        # self.assertEqual(response.status_code, 200)
        print(response.content)
        descricoes = [curso['descricao'] for curso in response.json()['results']]
        self.assertIn('Python', descricoes)
