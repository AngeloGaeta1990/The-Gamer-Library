from django.test import TestCase
from .forms import AddGameForm
from .models import Platform
# Create your tests here.


class TestAddGameForm(TestCase):

    def setUp(self):
        # You can create a platform instance for testing
        self.platform = Platform.objects.create(name='PC', category='pc',
                                                slug='pc')

    def test_form_is_valid(self):
        game_form = AddGameForm({'name': 'Divinity 2 original sin',
                                 'platform': 'PC'})
        self.assertTrue(game_form.is_valid())
