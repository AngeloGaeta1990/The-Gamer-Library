from django.test import TestCase
from django.contrib.auth.models import User
from .forms import (AddPlatformForm, AddGameForm, AddWishlistGameForm,
                    EditGameForm, EditWishListGameForm, EditPlatformForm)
from .models import Platform, Game, WishListGame
# Create your tests here.


class TestAddPlatformForm(TestCase):
    """
    Test class for the AddPlatformForm form.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='myUsername', password='myPassword')

    def test_form_is_valid(self):
        """
        Test validity of add platform form.
        """
        platform_form = AddPlatformForm(data={
            'name': 'PC',
            'category': 'pc',
        })
        self.assertTrue(platform_form.is_valid())


class TestEditPlatformForm(TestCase):
    """
    Test class for the EditPlatformForm form.
    """
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
        """
        Test validity of edit platform form.
        """
        updated_data = {
            'name': 'Updated PC',
            'category': 'pc',
            'image': 'updated_image.jpg',
            'box_color': '#00ff00',
            'font_color': '#000000',
            'operative_systems': 'Windows',
            'gpu': 'GTX 3080',
            'cpu': 'Intel Core i9',
            'ram': 32,
            'disk_size': 1000,
            'disk_type': 'SSD',
        }
        edit_platform_form = EditPlatformForm(instance=self.platform,
                                              data=updated_data)
        self.assertTrue(edit_platform_form.is_valid())


class TestAddGameForm(TestCase):
    """
    Test class for the AddGameForm form.
    """

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
        """
        Test validity of add game form.
        """
        game_form = AddGameForm(user=self.user, data={
            'name': 'Divinity 2 original sin',
            'platform': self.platform.id,
        })
        self.assertTrue(game_form.is_valid())


class TestEditGameForm(TestCase):
    """
    Test class for the EditGameForm form.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='myUsername', password='myPassword')
        self.platform = Platform.objects.create(name='PC', category='pc',
                                                slug='pc', user=self.user)
        self.game = Game.objects.create(name='Test Game',
                                        platform=self.platform,
                                        slug='test-game', user_score=70)

    def test_form_is_valid(self):
        """
        Test validity of edit game form.
        """
        updated_data = {
            'name': 'Updated Game',
            'platform': self.platform.id,
            'user_score': 80,
            'metacritic_score': 85,
            'developer': 'New Developer',
            'genres': 'Action',
            'release_date': '2023-01-01',
            'completion_date': '2023-01-15',
            'hours_spent': 20,
            'user_review': 'Great game!',
        }
        edit_game_form = EditGameForm(instance=self.game, data=updated_data)
        self.assertTrue(edit_game_form.is_valid())


class TestAddWishlistGameForm(TestCase):
    """
    Test class for the AddWishlistGameForm form.
    """

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
        """
        Test validity of add wishlist game form.
        """
        wishlist_game_form = AddWishlistGameForm(user=self.user, data={
            'name': 'New Wishlist Game',
            'platform': self.platform.id,
            'priority': 1,
        })
        self.assertTrue(wishlist_game_form.is_valid())


class TestEditWishListGameForm(TestCase):
    """
    Test class for the EditWishListGameForm form.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='myUsername', password='myPassword')
        self.platform = Platform.objects.create(name='PC', category='pc',
                                                slug='pc', user=self.user)
        self.wishlist_game = WishListGame.objects.create(
            name='Test Wishlist Game',
            platform=self.platform,
            priority=1,
            currency='$',
            cost=19.99,
            store='Epic',
        )

    def test_form_is_valid(self):
        """
        Test validity of edit wishlist game form.
        """
        edit_wishlist_game_form = EditWishListGameForm(data={
            'name': 'Updated Wishlist Game',
            'platform': self.platform.id,
            'store': 'Steam',
            'priority': 2,
            'currency': '£',
            'cost': 24.99,
        }, instance=self.wishlist_game)
        self.assertTrue(edit_wishlist_game_form.is_valid())
