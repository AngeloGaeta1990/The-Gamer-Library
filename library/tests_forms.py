from django.test import TestCase
from django.contrib.auth.models import User
from .forms import AddGameForm
from .models import Platform
# Create your tests here.


class TestAddGameForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='myUsername', password='myPassword')
        self.platform = Platform.objects.create(name='PC', category='pc',
                                                slug='pc', user=self.user)

    def test_form_is_valid(self):
        game_form = AddGameForm(user=self.user, data={
            'name': 'Divinity 2 original sin',
            'platform': self.platform.id,
        })
        self.assertTrue(game_form.is_valid())
