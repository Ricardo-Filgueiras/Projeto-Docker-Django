from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import SecureLoginForm, UserRegisterForm, UserUpdateForm
from .models import UserProfile


class AutomaticUserProfileCreationTest(TestCase):
    """Testes para criação automática de UserProfile via signals"""
    
    def test_userprofile_created_on_user_creation(self):
        """Testa se UserProfile é criado automaticamente quando um User é criado"""
        user = User.objects.create_user(
            username='newuser',
            email='new@example.com',
            password='testpass123'
        )
        # Verifica se o profile foi criado automaticamente
        self.assertTrue(hasattr(user, 'profile'))
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.profile.user, user)


class UserProfileModelTest(TestCase):
    """Testes para o modelo UserProfile"""
    
    def setUp(self):
        """Cria um usuário de teste"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = self.user.profile
    
    def test_profile_creation(self):
        """Testa criação de perfil do usuário"""
        self.assertIsNotNone(self.profile)
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertIsNotNone(self.profile.created_at)

    def test_profile_timestamps(self):
        """Testa se created_at e updated_at funcionam"""
        self.assertIsNotNone(self.profile.created_at)
        self.assertIsNotNone(self.profile.updated_at)
        self.assertEqual(self.profile.created_at, self.profile.updated_at)


class SecureLoginFormTest(TestCase):
    """Testes para a form de login seguro"""
    
    def setUp(self):
        """Cria um usuário de teste"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login_with_valid_credentials(self):
        """Testa login com credenciais válidas"""
        form = SecureLoginForm(data={
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertTrue(form.is_valid())

    def test_login_with_nonexistent_user(self):
        """Testa login com usuário que não existe - deve usar mensagem genérica"""
        form = SecureLoginForm(data={
            'username': 'nonexistent',
            'password': 'anypassword'
        })
        self.assertFalse(form.is_valid())
        # Valida que a mensagem é genérica (não revela se o usuário existe)
        self.assertIn('Esse usuário ou senha estão incorretos', str(form.errors))

    def test_login_with_incorrect_password(self):
        """Testa login com senha incorreta - deve usar mensagem genérica"""
        form = SecureLoginForm(data={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertFalse(form.is_valid())
        # Valida que a mensagem é genérica (não diferencia usuário vs senha)
        self.assertIn('Esse usuário ou senha estão incorretos', str(form.errors))

    def test_login_with_empty_username(self):
        """Testa login com username vazio"""
        form = SecureLoginForm(data={
            'username': '',
            'password': 'testpass123'
        })
        self.assertFalse(form.is_valid())

    def test_login_with_empty_password(self):
        """Testa login com password vazio"""
        form = SecureLoginForm(data={
            'username': 'testuser',
            'password': ''
        })
        self.assertFalse(form.is_valid())


class LoginViewTest(TestCase):
    """Testes para a view de login"""
    
    def setUp(self):
        """Configura cliente de teste e usuário"""
        self.client = Client()
        self.login_url = reverse('usuario:login')
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login_page_loads(self):
        """Testa se a página de login carrega"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuario/login.html')

    def test_successful_login_redirect(self):
        """Testa se login bem-sucedido redireciona"""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        }, follow=True)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_failed_login_displays_error(self):
        """Testa se login falhado exibe mensagem de erro genérica"""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, 'Esse usuário ou senha estão incorretos')

    def test_nonexistent_user_displays_error(self):
        """Testa se tentativa com usuário inexistente exibe mensagem genérica"""
        response = self.client.post(self.login_url, {
            'username': 'nonexistent',
            'password': 'anypassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, 'Esse usuário ou senha estão incorretos')


class UserRegisterFormTest(TestCase):
    """Testes para a form de registro - incluindo validação de email único"""
    
    def setUp(self):
        """Cria um usuário existente"""
        self.existing_user = User.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpass123'
        )
    
    def test_register_with_valid_data(self):
        """Testa registro com dados válidos"""
        form = UserRegisterForm(data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertTrue(form.is_valid())

    def test_register_with_mismatched_passwords(self):
        """Testa registro com senhas diferentes"""
        form = UserRegisterForm(data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'DifferentPass123!'
        })
        self.assertFalse(form.is_valid())

    def test_register_with_invalid_email(self):
        """Testa registro com email inválido"""
        form = UserRegisterForm(data={
            'username': 'newuser',
            'email': 'invalid-email',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertFalse(form.is_valid())
    
    def test_register_with_existing_email(self):
        """Testa registro com email que já existe - REGRA DE UNICIDADE"""
        form = UserRegisterForm(data={
            'username': 'differentuser',
            'email': 'existing@example.com',  # Email já usado
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Este email já está registrado', str(form.errors))
    
    def test_register_with_existing_username(self):
        """Testa registro com username que já existe"""
        form = UserRegisterForm(data={
            'username': 'existinguser',  # Username já usado
            'email': 'different@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Este username já está em uso', str(form.errors))


class UserUpdateFormTest(TestCase):
    """Testes para a form de atualização de perfil - incluindo validação de email único"""
    
    def setUp(self):
        """Cria usuários de teste"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpass123'
        )

    def test_update_with_valid_data(self):
        """Testa atualização com dados válidos"""
        form = UserUpdateForm(data={
            'username': 'testuser',
            'email': 'newemail@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_update_missing_email(self):
        """Testa atualização sem email"""
        form = UserUpdateForm(data={
            'username': 'testuser',
            'email': '',
            'first_name': 'John',
            'last_name': 'Doe'
        }, instance=self.user)
        self.assertFalse(form.is_valid())
    
    def test_update_with_existing_email_another_user(self):
        """Testa atualização usando email de outro usuário - REGRA DE UNICIDADE"""
        form = UserUpdateForm(data={
            'username': 'testuser',
            'email': 'other@example.com',  # Email de outro usuário
            'first_name': 'John',
            'last_name': 'Doe'
        }, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('Este email já está registrado por outro usuário', str(form.errors))
    
    def test_update_can_keep_own_email(self):
        """Testa que o usuário pode manter seu próprio email"""
        form = UserUpdateForm(data={
            'username': 'testuser',
            'email': 'test@example.com',  # Seu próprio email
            'first_name': 'John',
            'last_name': 'Doe'
        }, instance=self.user)
        self.assertTrue(form.is_valid())