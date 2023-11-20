from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class UserLoginTestCase(TestCase):
    def setUp(self):
        # Configuración inicial, crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login_success(self):
        # Prueba el inicio de sesión exitoso
        url = reverse('user_login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  

    def test_user_login_failure(self):
        # Prueba el inicio de sesión fallido
        url = reverse('user_login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Nombre de usuario o contraseña incorrectos.')

    def test_user_login_form_displayed(self):
        # Prueba que el formulario de inicio de sesión se muestra correctamente
        url = reverse('user_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'username')
        self.assertContains(response, 'password')